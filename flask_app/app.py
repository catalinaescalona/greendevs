# Prior to running pip install all modules in requirements.txt using the following command:
# pip install -r requirements.txt

###### To run locally ######
# Pull the latest commits.
# Change working directory to ..greendevs/flask_app/
# Use the following command: flask run
# you can now test the website using http://127.0.0.1:5000/
# if you get a 403 error (Access to 127.0.0.1 was denied), you may need to clear cookies.

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/routes')
def hello_world():
    return '''Here is a list of all routes currently created in Pollaris: <br>
    /<br>
    /login<br>
    /vote<br>
    /create<br>
    /popular
    '''

@app.route('/')
def index(name=None):
    '''Renders an HTML template with the Pollaris Homepage'''
    return render_template("homepage.html", name=name)

@app.route('/login')
def log_in(name=None):
    '''Renders an HTML template with Pollaris login page'''
    return render_template("login_page.html", name=name)

@app.route('/vote')
def take_a_poll(name=None):
    '''Renders an HTML template that allows users to vote in an existing poll'''
    return render_template("voting_page.html", name=name)

@app.route('/create')
def create_poll(name=None):
    '''Renders an HTML template that allows users to create a poll'''
    return render_template("create_poll.html", name=name)

@app.route('/popular')
def popular_polls(name=None):
    '''Renders an HTML template that displays popular, already-existing polls for users to browse and take'''
    return render_template("popular_polls.html", name=name)

# add GET/POST with login info? and figure out how to do sign up / account creation
# @app.route('/signup')
# def sign_up():
#     return "This is where you will create a new account!"

# @app.route('/user')
# def user_dashboard():
#     return "This is your dashboard where you will be able to access all of your polls and history!"