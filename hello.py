"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

def login():
    if request.method == 'POST':
        check_exist()
    else:
        show_the_login_form()

@app.route('/play')
@app.route('/hello/<string:name>/')
def hello(name=None):
    return render_template('hello.html', name = name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
def check_exist():
    pass

def show_the_login_form():
    pass

if __name__ == '__main__':
    app.run()
