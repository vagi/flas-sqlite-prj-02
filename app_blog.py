# Import required libraries
from flask import Flask, render_template, request, make_response, session, redirect, url_for
import sqlite3
from datetime import datetime

# Initialize Flask object
app = Flask(__name__)

"""
Скрипт для создания базы данных и таблицы                                                  |
"""
connection = sqlite3.connect('blog.sqlite')

cursor = connection.cursor()

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
        new_post_title = request.form['title']
        new_post_description = request.form['description']

        # Checking whether ttile or description are empty
        if not new_post_title or new_post_description:
            return "<i>Empty title or description sent!</i>"
        else:
            # Passing the received text to the database




            # Now redirect to the main page with all posts
            return redirect('/index')















# Inserting condition in case this file is used as a module (imported by another file)
if __name__ == '__main__':
    app.run(debug=True)  # When deployed on server this to be changed to False
