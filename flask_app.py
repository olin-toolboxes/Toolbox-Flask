"""
Put your Flask app code here.
"""
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def profile():
    for key in request.form.keys():
        if request.form[key] is ' ':
            return "Error, please input all form fields"
    return render_template('info.html',
                            name_user = request.form['name'],
                            age_user = request.form['age'],
                            ninja = request.form['fav_ninja'])

    #check they exist
    #send to profile html page


if __name__ == '__main__':
    app.run()
