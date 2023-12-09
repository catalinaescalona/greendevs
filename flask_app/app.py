# Prior to running pip install all modules in requirements.txt using the following command:
# pip install -r requirements.txt

###### To run locally ######
# Pull the latest commits.
# Change working directory to ..greendevs/flask_app/
# Use the following command: flask run
# you can now test the website using http://127.0.0.1:5000/
# if you get a 403 error (Access to 127.0.0.1 was denied), you may need to clear cookies.

from flask import Flask, url_for, request, render_template, redirect
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

@app.route('/login', methods=['GET', 'POST'])
def log_in(name=None):
    '''
    This function checks log in credentials when a user attempts to log in.
    It Queries the database for the credentials. 
    If credentials exist, user is redirected to user/<user_name>. Otherwise login error message is displayed.
    '''
    # Get input from user --- python input statements will need to be replaced with GET requests
    username = input("Please enter your user name: ")
    password = input("Please enter your password: ")
    
    if request.method == 'POST' and 'user_name' in request.form and 'password' in request.form:
        # Connect to databse
        conn = sqlite3.connect("db", timeout=10)
        c = conn.cursor()
        
        # Create string to query database for login credentials and execute query
        login_query = '''SELECT user_name, password FROM Users WHERE user_name="{}" AND password="{}";'''.format(username, password)
        c.execute(login_query)
        result = c.fetchone()
        # Close database
        conn.close()

        # If the credentials don't match, the result=c.fetchone() function will return nothing.
        if not result:
            # display log in error message
            render_template("login_page.html", name=name, message="Incorrect username or password.")
        else:
            #redirect to user/<user_name>
            return redirect(url_for(user_page, user_name=user_name))
            
    '''Renders an HTML template with Pollaris login page'''
    return render_template("login_page.html", name=name)

@app.route('/user/<user_name>')
def user_page(user_name):
    return "<h1>"+str(user_name)+"<\h1>"

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
