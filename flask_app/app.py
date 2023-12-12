# Prior to running pip install all modules in requirements.txt using the following command:
# pip install -r requirements.txt

###### To run locally ######
# Pull the latest commits.
# Change working directory to ..greendevs/flask_app/
# Use the following command: flask run
# you can now test the website using http://127.0.0.1:5000/
# if you get a 403 error (Access to 127.0.0.1 was denied), you may need to clear cookies.

from flask import Flask, url_for, request, render_template, redirect, jsonify
import sqlite3
from random import randint
import datetime
import psycopg2

app = Flask(__name__)

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://pollaris_db_user:wzlXGhePudWAa8KTs0DKAzIRnoNVrEOp@dpg-clrjq9pjvg7s73ei8g0g-a/pollaris_db")
    conn.close()
    return 'Database Connection Successful'
    
@app.route('/routes')
def hello_world():
    return '''Here is a list of all routes currently created in Pollaris: <br>
    /routes<br>
    /<br>
    /signup<br>
    /login<br>
    /user/&lt;user_name&gt;<br>
    /create<br>
    /vote<br>
    /popular
    '''

@app.route('/')
def index(name=None):
    '''Renders an HTML template with the Pollaris Homepage'''
    return render_template("homepage.html", name=name)

# @app.route('/signup', methods=['GET', 'POST'])
# def sign_up():
#     '''
#     This function adds a new user to the database
#     '''
#     if request.method == 'POST' and 'User Name' in request.form and 'Password' in request.form and 'Email' in request.form and 'First' in
#     request.form and 'Last' in request.form:
#         # Store form inputs as variables
#         user_name = request.form['User Name']
#         password = request.form['Password']
#         email = request.form['Email']
#         first = request.form['First']
#         last = request.form['Last']

#         # user_id must be unique!
#         # Create random 9-digit id for user_id. Query database to see if id exists already.
#         new_id = randint(100000000, 999999999)
#         result = c.execute("SELECT * FROM Users WHERE user_id='{}'".format(new_id)).fetchone()
        
#         c.execute will return nothing if the id does not exist.
#         #If user_id already exists, randomly select new 9-digit id until one is chose that does not exist already.
#         if result != None:
#             while result != None:
#                 new_id = randint(100000000, 999999999)
#                 result = c.execute("SELECT * FROM Users WHERE user_id='{}'".format(new_id)).fetchone()

#         # user_name must be unique. return error message indicating user name is taken if not unique
#         new_name = c.execute("SELECT * FROM Users WHERE user_name='{}'".format(user_name)).fetchone()
#         if new_name != None:
#             return render_template('sign_up.html', message="User name taken. Please try again.")
#         # Chech regex match to verify valid email address.
#         if not re.match(r'^[A-Za-z\.!#$%\*0-9]+@[A-Za-z0-9]+\.[a-zA-Z]{2,3}$', email):
#             return render_template('sign_up.html', message="Please enter a valid email.")
#         # email must be unique. return error message if email is associated with an account
#         new_email = c.execute("SELECT * FROM Users WHERE user_name='{}'".format(email)).fetchone()
#         if new_email = None:
#             return render_template('sign_up.html', message="Email address already associated with an account. Please try again.")
        
#         timestamp = datetime.datetime.now()

#         # Connect to database
#         conn = psycopg2.connect("postgres://pollaris_db_user:wzlXGhePudWAa8KTs0DKAzIRnoNVrEOp@dpg-clrjq9pjvg7s73ei8g0g-a/pollaris_db")
#         c = conn.cursor()
        
#         #insert values into table
#         sql = "INSERT INTO Users VALUES (?, ?, ?, ?, ?, ?, ?)"
#         new_user = (new_id, user_name, first, last, email, password, timestamp)
#         c.execute(sql, new_user)
        
#         # Commit changes and close database
#         conn.commit()
#         conn.close()

#         return redirect(url_for(user_page, user_name=user_name))
#     else:
#         return render_template('sign_up.html', message='please complete the form')
#     return render_template('sign_up.html')

# @app.route('/login', methods=['GET', 'POST'])
# def log_in(name=None):
#     '''
#     This function checks log in credentials when a user attempts to log in.
#     It Queries the database for the credentials. 
#     If credentials exist, user is redirected to user/<user_name>. Otherwise login error message is displayed.
#     '''
#     if request.method == 'POST' and 'user_name' in request.form and 'password' in request.form:
#         # Connect to databse
#         conn = psycopg2.connect("postgres://pollaris_db_user:wzlXGhePudWAa8KTs0DKAzIRnoNVrEOp@dpg-clrjq9pjvg7s73ei8g0g-a/pollaris_db")
#         c = conn.cursor()

#         user_name = request.form['username']
#         password = request.form['password']
        
#         # Create string to query database for login credentials and execute query
#         login_query = '''SELECT user_name, password FROM Users WHERE user_name="{}" AND password="{}";'''.format(user_name, password)
#         c.execute(login_query)
#         result = c.fetchone()
#         # Close database
#         conn.close()

#         # If the credentials don't match, the result=c.fetchone() function will return nothing.
#         if not result:
#             # display log in error message
#             render_template("login_page.html", name=name, message="Incorrect username or password.")
#         else:
#             #redirect to user/<user_name>
#             return redirect(url_for(user_page, user_name=user_name))
#     return render_template("login_page.html", name=name)

@app.route('/user/<user_name>')
def user_page(user_name):
    '''Temporary function that will eventually render an HTML template that displays user's profile page'''
    message = "<h1>"
    message += str(user_name)
    message += "</h1>"
    return message

@app.route('/create')
def create_poll(name=None):
    '''Renders an HTML template that allows users to create a poll'''
    return render_template("create_poll.html", name=name)

@app.route('/vote')
def take_a_poll(name=None):
    '''Renders an HTML template that allows users to vote in an existing poll'''
    return render_template("voting_page.html", name=name)

@app.route('/popular')
def popular_polls(name=None):
    '''Renders an HTML template that displays popular, already-existing polls for users to browse and take'''
    return render_template("popular_polls.html", name=name)
