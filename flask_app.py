"""
Put your Flask app code here.
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    make_profile()
    return render_template('survey.html')

@app.route('/user', methods=['GET', 'POST'])
def make_profile():
    print('hello')
    try:
        name = request.form['name']
        age = request.form['age']
        return render_template('profile.html', name=name, age=age)
    except:
        return

@app.route('/error')
def error():
    return render_template('error.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
