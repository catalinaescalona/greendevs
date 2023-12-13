# Prior to running pip install all modules in requirements.txt using the following command:
# pip install -r requirements.txt

###### To run locally ######
# Pull the latest commits.
# Change working directory to ..greendevs/flask_app/
# Use the following command: flask run
# you can now test the website using http://127.0.0.1:5000/
# if you get a 403 error (Access to 127.0.0.1 was denied), you may need to clear cookies.

from flask import Flask, url_for, request, render_template, redirect, jsonify, session, flash
import sqlite3
from random import randint
from datetime import datetime

app = Flask(__name__)
app.secret_key = "top_secret_password"

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

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    '''
    This function adds a new user to the database.
    '''
    if "username" in session:
        return redirect(url_for("user_page", user_name=session['username']))
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'first' in request.form and 'last' in request.form:
        # Store form inputs as variables
        user_name = request.form['username']
        password = request.form['password']
        email = request.form['email']
        first = request.form['first']
        last = request.form['last']
        timestamp = datetime.datetime.now()
        
        # Connect to database
        conn = sqlite3.connect("db", timeout=10)
        c = conn.cursor()
        
        # user_id must be unique!
        # Create random 9-digit id for user_id. Query database to see if id exists already.
        new_id = randint(100000000, 999999999)
        result = c.execute("SELECT * FROM Users WHERE user_id='{}'".format(new_id)).fetchone()
        
        # c.execute will return nothing if the id does not exist.
        # If user_id already exists, randomly select new 9-digit id until one is chose that does not exist already.
        if result != None:
            while result != None:
                new_id = randint(100000000, 999999999)
                result = c.execute("SELECT * FROM Users WHERE user_id='{}'".format(new_id)).fetchone()

        # user_name must be unique. return error message indicating user name is taken if not unique
        new_name = c.execute("SELECT * FROM Users WHERE user_name='{}'".format(user_name)).fetchone()
        if new_name != None:
            return render_template('sign_up.html', message="User name taken. Please try again.")
        # Chech regex match to verify valid email address.
        if not re.match(r'^[A-Za-z\.!#$%\*0-9]+@[A-Za-z0-9]+\.[a-zA-Z]{2,3}$', email):
            return render_template('sign_up.html', message="Please enter a valid email.")
        # email must be unique. return error message if email is associated with an account
        new_email = c.execute("SELECT * FROM Users WHERE user_name='{}'".format(email)).fetchone()
        if new_email == None:
            return render_template('sign_up.html', message="There is an email address associated with an account.")
        
        #insert values into table
        sql = "INSERT INTO Users VALUES (?, ?, ?, ?, ?, ?, ?)"
        new_user = (new_id, user_name, first, last, email, password, timestamp)
        c.execute(sql, new_user)
        
        # Commit changes and close database
        conn.commit()
        conn.close()

        session['username'] = user_name
        return redirect(url_for("user_page", user_name=user_name))
    else:
        return render_template('sign_up.html', message='Incomplete Form.')
    return render_template('sign_up.html')

@app.route('/login', methods=['GET', 'POST'])
def log_in(name=None):
    '''
    This function checks log in credentials when a user attempts to log in.
    It Queries the database for the credentials. 
    If credentials exist, user is redirected to user/<user_name>. Otherwise login error message is displayed.
    '''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Connect to databse
        conn = sqlite3.connect("db", timeout=10)
        c = conn.cursor()

        # Create string to query database for login credentials and execute query
        login_query = '''SELECT user_name, password 
                         FROM Users 
                         WHERE user_name="{}" AND password="{}";'''.format(request.post['username'], request.post['password'])
        c.execute(login_query)
        result = c.fetchone()
        # Close database
        conn.close()

        # If the credentials don't match, the result=c.fetchone() function will return nothing.
        if not result:
            # display log in error message
            render_template("login_page.html", message="Incorrect username or password.")
        else:
            #start session and redirect to user/<user_name>
            session["username"] = request.post['username']
            return redirect(url_for("user_page", user_name=user_name))
    elif "username" in session:
        redirect(url_for("user_page", user_name=user_name))
    else:
        return render_template("login_page.html")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for("login"))

@app.route('/user/<user_name>')
def user_page(user_name):
    '''Temporary function that will eventually render an HTML template that displays user's profile page'''
    if "username" in session:
        message = "<h1>"
        message += str(session['username'])
        message += "</h1>"
        return message
    else:
        redirect(url_for("login"))


@app.route('/create', methods=["GET", "POST"])
def create_poll(name=None):
    if request.method=="POST":
        data=request.form
        print(data)
    '''Renders an HTML template that allows users to create a poll'''
    return render_template("create_poll.html", name=name)

#Need to find way to access poll_id
@app.route('/vote')
def take_a_poll(name=None, poll_id):
    conn = psycopg2.connect("postgres://pollaris_db_user:wzlXGhePudWAa8KTs0DKAzIRnoNVrEOp@dpg-clrjq9pjvg7s73ei8g0g-a/pollaris_db")
    c = conn.cursor()

    c.execute('''SELECT json FROM Polls WHERE poll_id="{}"'''.format(poll_id))
    json = c.fetchone()[0]

    conn.close()

    if request.method == "POST":
        conn = psycopg2.connect("postgres://pollaris_db_user:wzlXGhePudWAa8KTs0DKAzIRnoNVrEOp@dpg-clrjq9pjvg7s73ei8g0g-a/pollaris_db")
        c = conn.cursor()
        c.execute('''SELECT user_id FROM Users WHERE username="{}"'''.format(session['username']))
        
        user_id = c.fetchone()[0]
        
        #Get javascript dict somehow and add it here.
        responses = request.form["answers"]
        
        for q_no, answer in responses:
            new_id = randint(100000000, 999999999)
            result = c.execute("SELECT * FROM Users WHERE user_id='{}'".format(new_id)).fetchone()
            
            # c.execute will return nothing if the id does not exist.
            # If user_id already exists, randomly select new 9-digit id until one is chose that does not exist already.
            if result != None:
                while result != None:
                    new_id = randint(100000000, 999999999)
                    result = c.execute("SELECT * FROM Users WHERE user_id='{}'".format(new_id)).fetchone()
            question_id = q_no
            option_id = answer
            vote_created = datetime.datetime.now()
                
            vote = vote_id, user_id, poll_id, question_id, option_id, vote_created
            c.execute("INSERT INTO Votes VALUES (?, ?, ?, ?, ?, ?);", (vote))
            conn.commit()
        conn.close()

    '''Renders an HTML template that allows users to vote in an existing poll'''
    return render_template("voting_page.html", name=name, questions=json)

@app.route('/popular')
def popular_polls(name=None):
    '''Renders an HTML template that displays popular, already-existing polls for users to browse and take'''
    return render_template("popular_polls.html", name=name)
