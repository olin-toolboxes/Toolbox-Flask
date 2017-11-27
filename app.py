"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
app = Flask(__name__)
name = ''
age = ''
@app.route('/login', methods=['GET', 'POST'])
def login():
    global name, age
    name = request.form['name']
    age = request.form['age']
    fav = request.form['fav']

    x = int(age)
    print(x)
    if x<100:
        print('yeeee')
        if fav == 'Emily':
            return render_template('profile.html', name = name, age = age)
        else:
            return render_template('error_page.html', name = name, age = age)
    else:
        print('here')
        return render_template('missing.html')

@app.route('/missing', methods=['GET', 'POST'])
def missing():
    render_template('missing.html')

@app.route('/redo', methods=['GET', 'POST'])
def redo():
    global name, age
    fav = request.form['fav']

    if fav == 'Emily':
        return render_template('profile.html', name = name, age = age)
    else:
        return render_template('error_page.html', name = name, age = age)

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
