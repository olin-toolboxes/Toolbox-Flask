"""
Put your Flask app code here.
"""

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.form['name'] and request.form['age'] and request.form['faveninja']:
        name = request.form['name']
        age = request.form['age']
        return render_template('profile.html', name=name, age=age)
    else:
        return render_template('error.html')


if __name__ == '__main__':
    app.run()
