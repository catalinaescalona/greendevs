# Prior to running pip install all modules in requirements.txt using the following command:
# pip install -r requirements.txt

###### To run locally ######
# Pull the latest commits.
# Change working directory to ..greendevs/flask_app/
# Use the following command: flask run
# you can now test the website using http://127.0.0.1:5000/
# if you get a 403 error (Access to 127.0.0.1 was denied), you may need to clear cookies.

from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''Welcome to Pollaris!<br><br>
    Here is a list of all routes currently created: <br>
    /<br>
    /login<br>
    /signup<br>
    /take<br>
    /user<br>
    /create<br>
    '''

@app.route('/login')
def log_in():
    return "This is where you will log in!"

@app.route('/signup')
def sign_up():
    return "This is where you will create a new account!"

@app.route('/take')
def take_a_poll():
    return "This is where you will be able to find a poll to take!"

@app.route('/user')
def user_dashboard():
    return "This is your dashboard where you will be able to access all of your polls and history!"

@app.route('/create')
def create_poll():
    return "This is where you will create a new poll!"
