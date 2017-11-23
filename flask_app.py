"""
Put your Flask app code here.
"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.form['name'] and request.form['age'] and request.form['ninja']:   # if all inputs are given
        name = request.form['name']
        age = request.form['age']
        ninja = request.form['ninja']
        if check_exist(ninja):                                                  # if NINJA choice valid
            return render_template('profile.html', name = name, age = age)
        else:                                                                   # redirect to hello page if credentials invalid
            error = 'Invalid Entry'
            return render_template('profile.html',name = name, age = age, error=error)
    else:
        return '''
         <h1>Error: Did not include all required info !</h1>

        <form action="/" method="GET">
          <input type="submit" value="Return to Home">
        </form>
        '''

def check_exist(ninja):
    ninjas = ['Emily', 'Duncan', 'Hannah', 'Matt', 'Seungin', 'Tony']
    if ninja in ninjas:
        return True
    else:
        return False

@app.route('/')
def main():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()
