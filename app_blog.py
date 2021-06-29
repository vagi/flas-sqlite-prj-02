# Import required libraries
from flask import Flask, render_template, request, make_response, session, redirect, url_for
import sqlite3
from datetime import datetime, date

# Initialize Flask object
app = Flask(__name__)


# Uncomment to create a table
""" 
    connection = sqlite3.connect('blog.sqlite')
    cursor = connection.cursor()
    # Script for creation of a new table in the database
    cursor.execute("CREATE TABLE IF NOT EXISTS posts (id integer primary key AUTOINCREMENT, title varchar(100), description varchar(200), date datetime)")
    connection.commit()
    connection.close()
"""

# A decorator used to tell the application which URL
# is associated with the following function
@app.route('/')
@app.route('/index')
def show_all_posts():
    """
    The function loads all posts from specified table of the database.
    Returns:
        the main index.HTML page to be loaded with all posts
    """
    # Coonection to the database
    connection = sqlite3.connect('blog.sqlite')
    # Initialization of cursor for operation procedure
    cursor = connection.cursor()
    # Writing SQL template that will get data from all columns of the table
    cursor.execute("SELECT * FROM posts")
    # Fetching all data
    all_posts = cursor.fetchall()
    # Closing the connection
    connection.close()
    # Returning main HTML page with all posts
    return render_template('index.html', posts=all_posts)


# A decorator used to tell the application which URLs is
# associated with the following function
@app.route('/index/add_post', methods=('GET', 'POST'))
def add_new_post():
    """
    In case of GET request this function loads add_post.html with the <form>>.
    Once a POST request sent, gets two parameters (str) from
    the Form and pass it to the database.
    Returns:
        redirects to the main HTML page with all posts
    """
    if request.method == 'GET':
        return render_template('add_post.html',)
    else:
        # Getting input of title and description from the <form>
        new_title = request.form['title']
        new_description = request.form['description']

        # Checking whether title or description of post are empty
        if not new_title or not new_description:
            return "<i>Please fill in the title and the description of your post!</i>"
        else:
            # Opening connection to the database
            connection = sqlite3.connect('blog.sqlite')
            # Initialization of cursor for operation procedure
            cursor = connection.cursor()
            # Creatiing tuple with parameters
            values = (new_title, new_description, date.today())
            # Arranging template of SQL request to write in the data and
            # passing the tuple with params to it
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


# A decorator used to tell the application which URLs is
# associated with the following function
@app.route('/index/edit_post', methods=('GET', 'POST'))
def edit_post():
    """
    In case of GET request this function loads edit_post.html with the <form>.
    Once a POST request sent, gets one mandatory parameter and two optional
    parameters from the <form> and pass it to the database.
    Returns:
        the main HTML page to be loaded with all posts
    """
    if request.method == 'GET':
        return render_template('edit_post.html',)
    else:
        # Getting input of id, text and description from the <form>
        post_id = request.form['id']
        post_title = request.form['title']
        post_description = request.form['description']

        # Checking whether id of post is empty
        if not post_id:
            return "<i>Please enter ID of a post to be updated!</i>"
        else:
            # Opening connection to the database
            connection = sqlite3.connect('blog.sqlite')
            # Cursor initialization for procedure
            cursor = connection.cursor()
            # Creatiing tuple with parameters
            values = (post_title, post_description, post_id)
            # Arranging template of SQL request to update the data
            cursor.execute("""
                            UPDATE posts 
                            SET title=?, description=?
                            WHERE id=?
                            """, values)
            # Sending the data to database
            connection.commit()
            # Closing connection to the database
            connection.close()
    # Now redirect to the main page with all posts
    return redirect('/index')


# A decorator used to tell the application which URLs is
# associated with the following function
@app.route('/index/delete_post', methods=('GET', 'POST'))
def delete_post():
    """
    In case of GET request this function loads delete_post.html with the <form>.
    Once a POST request sent, gets one parameter (int) from
    the <form> and pass it to the database.
    Returns:
        the main HTML page to be loaded with all posts
    """
    if request.method == 'GET':
        return render_template('delete_post.html',)
    else:
        # Getting input of ID from the <form>
        post_id = request.form['id']
        # Checking whether ID of post is empty
        if not post_id:
            return "<i>Please enter ID of a post you want to delete!</i>"
        else:
            # Opening connection to the database
            connection = sqlite3.connect('blog.sqlite')
            # Cursor initialization for procedure
            cursor = connection.cursor()
            # Arranging template of SQL request to delete the data
            cursor.execute("""
                            DELETE FROM posts 
                            WHERE id=?
                            """, post_id)
            # Sending the data to database
            connection.commit()
            # Closing connection to the database
            connection.close()
    # Now redirect to the main page with all posts
    return redirect('/index')


# Inserting condition in case this file is used as a module (imported by another file)
if __name__ == '__main__':
    app.run(debug=True)  # When deployed on server this to be changed to False
