from flask import Flask, render_template, request
from DAL import *

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main.html')


"""signin page"""


@app.route('/signin', methods=['GET'])
def sign_in():
    return render_template('signin.html')


"""sign up"""


@app.route('/signup', methods=["GET"])
def sign_up():
    return render_template('signup.html')


"""find id/pw"""


@app.route('/find', methods=['GET'])
def find():
    return render_template('find.html')


"""login information"""


@app.route('/main', methods = ["POST"])
def login():
    id = request.form['id']
    pw = request.form['pw']
    print(id)
    print(pw)
    return render_template('main.html')


if __name__ == '__main__':
    app.run()
