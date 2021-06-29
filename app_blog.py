# Import required libraries
from flask import Flask, render_template, request, make_response, session, redirect, url_for
import sqlite3
from datetime import datetime, date

# Initialize Flask object
app = Flask(__name__)


connection = sqlite3.connect('blog.sqlite')

cursor = connection.cursor()

# Scrypt for creation of a new table in the database
cursor.execute("CREATE TABLE IF NOT EXISTS posts (id integer primary key AUTOINCREMENT, title varchar(100), description varchar(200), date datetime)")

connection.commit()

connection.close()

@app.route('/')
@app.route('/index')
def show_all_posts():
    # Подключение к базе данных
    connection = sqlite3.connect('blog.sqlite')
    # Инициализация курсора для выполнения операций
    cursor = connection.cursor()
    # в методе execute можно вставлять любые SQL команды
    cursor.execute("SELECT * FROM posts")
    # в случае если надо передать аргументы в строку
    # лучше это делать так, передавать аргумент
    # или список аргументов вторым параметром
    # пример:
    """
      если один параметр
      >>> cursor.execute("SELECT * FROM students WHERE id < ?", 10)
      если много параметров
      >>> cursor.execute("SELECT * FROM students WHERE id < ? AND id > ?", (10, 5))
    """

    # Далее чтобы забрать результат команды SELECT используем метод fetchall
    all_posts = cursor.fetchall()

    # Обязательно закрываем соединение
    connection.close()

    # Передаем список студентов в темплейт
    return render_template('index.html', posts=all_posts)


# A decorator used to tell the application which URLs is
# associated with the following function
@app.route('/add_post', methods=('GET', 'POST'))
def add_new_post():
    """
    In case of GET request this function loads add_post.html with the Form.
    Once a POST request sent, gets two parameters (str) from
    the Form and pass it to the database.
    Attributes:
        title (str): Text of new post title with length of 100 char
        description (str): Text of new post description with length 200 of char
    Returns:
        the main HTML page to be loaded with all posts
    """
    if request.method == 'GET':
        return render_template('add_post.html',)
    else:
        # Getting input of text and description in the <form>
        new_title = request.form['title']
        new_description = request.form['description']

        # Checking whether title or description of post are empty
        if not new_title or not new_description:
            return "<i>Please fill in the title and the description of your post!</i>"
        else:
            # Opening connection to the database
            connection = sqlite3.connect('blog.sqlite')

            # Инициализация курсора для выполнения операций
            cursor = connection.cursor()

            # Далее располагаем данные в том порядке в котором хотим записать в базу данных
            values = (new_title, new_description, date.today())

            # Arranging template of SQL request to write in the data
            cursor.execute("""INSERT INTO posts (id, title, description, date) 
                            VALUES (null, ?, ?, ?)""",
                            values
                )
            # Sending the data to database
            connection.commit()

            # Closing connection to the database
            connection.close()

            # Now redirect to the main page with all posts
            return redirect('/index')


# Inserting condition in case this file is used as a module (imported by another file)
if __name__ == '__main__':
    app.run(debug=True)  # When deployed on server this to be changed to False
