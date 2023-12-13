# Prior to running pip install all modules in requirements.txt using the following command:
# pip install -r requirements.txt

###### To run locally ######
# Pull the latest commits.
# Change working directory to ..greendevs/flask_app/
# Use the following command: flask run
# you can now test the website using http://127.0.0.1:5000/
# if you get a 403 error (Access to 127.0.0.1 was denied), you may need to clear cookies.

from flask import Flask, url_for, request, render_template, redirect, jsonify, session
import sqlite3
from random import randint
import datetime
import psycopg2
import re

app = Flask(__name__)
    
@app.route('/routes')
def hello_world():
    return '''Here is a list of all routes currently created in Pollaris: <br>
    /routes<br>
    /db_test<br>
    /<br>
    /login<br>
    /signup<br>
    /user/&lt;user_name&gt;<br>
    /create<br>
    /vote<br>
    /popular
    '''

@app.route('/db_test')
def testing():
    '''This function tests the connection to the database hosted on Render'''
    conn = psycopg2.connect("postgres://pollaris_db_user:wzlXGhePudWAa8KTs0DKAzIRnoNVrEOp@dpg-clrjq9pjvg7s73ei8g0g-a/pollaris_db")
    conn.close()
    return 'Database Connection Successful'

@app.route('/')
def index(name=None):
    conn = psycopg2.connect("postgres://pollaris_db_user:wzlXGhePudWAa8KTs0DKAzIRnoNVrEOp@dpg-clrjq9pjvg7s73ei8g0g-a/pollaris_db")
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE IF NOT EXISTS Users(user_id INT NOT NULL, 
                                                      user_name VARCHAR(30), 
                                                      first_name VARCHAR(50), 
                                                      last_name VARCHAR(50),
                                                      email VARCHAR(100) NOT NULL,
                                                      password VARCHAR(60) NOT NULL,
                                                      member_since VARCHAR(60),
                                        
                                                      PRIMARY KEY (user_id)
                 );''')
    
        c.execute('''CREATE TABLE IF NOT EXISTS Polls(poll_id INT,
                                                      user_id INT,
                                                      poll_data JSON,
                                                      poll_created VARCHAR(45),
                                                      
                                                      PRIMARY KEY (poll_id),
                                                      FOREIGN KEY (user_id) REFERENCES Users(user_id)
                );''')             
        
        c.execute('''CREATE TABLE IF NOT EXISTS Votes(vote_id INT,
                                                      user_id INT,
                                                      poll_id INT,
                                                      question_id INT,
                                                      option_id INT,
                                                      vote_created VARCHAR(45),
                                                      
                                                      PRIMARY KEY (vote_id),
                                                      FOREIGN KEY (user_id) REFERENCES Users(user_id),
                                                      FOREIGN KEY (poll_id) REFERENCES Polls(poll_id)
                 );''')
        
        conn.commit()
    except:
        pass
    conn.close()
    
    '''Renders an HTML template with the Pollaris Homepage'''
    return render_template("homepage.html", name=name)

@app.route('/redirect_home', methods=['GET'])
def redirect_home():
    response = {'home_url': url_for('index')}
    return jsonify(response)

@app.route('/redirect_login', methods=['GET'])
def redirect_login():
    response = {'login_url': url_for('log_in')}
    return jsonify(response)

@app.route('/login', methods=['GET', 'POST'])
def log_in(name=None):
    '''
    This function checks log in credentials when a user attempts to log in.
    It Queries the database for the credentials. 
    If credentials exist, user is redirected to user/<user_name>. Otherwise login error message is displayed.
    '''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Connect to databse
        conn = psycopg2.connect("postgres://pollaris_db_user:wzlXGhePudWAa8KTs0DKAzIRnoNVrEOp@dpg-clrjq9pjvg7s73ei8g0g-a/pollaris_db")
        c = conn.cursor()

        user_name = request.form['username']
        password = request.form['password']
        
        # Create string to query database for login credentials and execute query
        login_query = '''SELECT user_name, password FROM Users WHERE user_name="{}" AND password="{}";'''.format(user_name, password)
        c.execute(login_query)
        result = c.fetchone()
        # Close database
        conn.close()

        # If the credentials don't match, the result=c.fetchone() function will return nothing.
        if not result:
            # display log in error message
            return render_template('login_page.html', message="Incorrect Username and/or Password.")
        else:
            #redirect to user/<user_name>
            session["username"] = user_name
            return redirect(url_for('user_page', user_name=user_name))
    return render_template('login_page.html')

@app.route('/redirect_signup', methods=['GET'])
def redirect_signup():
    response = {'signup_url': url_for('sign_up')}
    return jsonify(response)

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    '''
    This function adds a new user to the database.
    '''
    if request.method == 'POST' and 'User Name' in request.form and 'Password' in request.form and 'Email' in request.form and 'First' in request.form and 'Last' in request.form:

        # Connect to database
        conn = psycopg2.connect("postgres://pollaris_db_user:wzlXGhePudWAa8KTs0DKAzIRnoNVrEOp@dpg-clrjq9pjvg7s73ei8g0g-a/pollaris_db")
        c = conn.cursor()
        
        # Store form inputs as variables
        user_name = request.form['username']
        password = request.form['password']
        email = request.form['email']
        first = request.form['first']
        last = request.form['last']

        # user_id must be unique!
        # Create random 9-digit id for user_id. Query database to see if id exists already.
        new_id = randint(100000000, 999999999)
        result = c.execute("SELECT * FROM Users WHERE user_id='{}'".format(new_id)).fetchone()
        
        # c.execute will return nothing if the id does not exist.
        #If user_id already exists, randomly select new 9-digit id until one is chose that does not exist already.
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
        if new_email != None:
            return render_template('sign_up.html', message="Email address already associated with an account. Please try again.")
        
        timestamp = datetime.datetime.now()

        #insert values into table
        sql = "INSERT INTO Users VALUES (?, ?, ?, ?, ?, ?, ?)"
        new_user = (new_id, user_name, first, last, email, password, timestamp)
        c.execute(sql, new_user)
        
        # Commit changes and close database
        conn.commit()
        conn.close()

        return redirect(url_for("user_page", user_name=user_name))
    else:
        return render_template('sign_up.html', message='please complete the form')
    return render_template('sign_up.html')

@app.route('/user/<user_name>')
def user_page(user_name):
    '''Temporary function that will eventually render an HTML template that displays user's profile page'''
    message = "<h1>"
    message += str(user_name)
    message += "</h1>"
    return message

@app.route('/redirect_create', methods=['GET'])
def redirect_create():
    response = {'create_url': url_for('create_poll')}
    return jsonify(response)

# GET AJAX METHOD TO WORK HERE
@app.route('/create', methods=["GET", "POST"])
def create_poll(name=None):
    if request.method=="POST":
        conn = psycopg2.connect("postgres:/pollaris_db_user:wzlXGhePudWAa8KTs0DKAzIRnoNVrEOp@dpg-clrjq9pjvg7s73ei8g0g-a/pollaris_db")
        c = conn.cursor()

        c.execute('''SELECT user_id FROM Users WHERE username="{}"'''.format(session['username']))
        user_id = c.fetchone()[0]
        
        poll_id = randint(100000000, 999999999)
        result = c.execute("SELECT * FROM Users WHERE user_id='{}'".format(new_id)).fetchone()
        
        # c.execute will return nothing if the id does not exist.
        # If user_id already exists, randomly select new 9-digit id until one is chose that does not exist already.
        if result != None:
            while result != None:
                poll_id = randint(100000000, 999999999)
                result = c.execute("SELECT * FROM Users WHERE user_id='{}'".format(new_id)).fetchone()
        
        #NEED TO GET THIS FROM JAVASCRIPT (test dictionary, but fill in with what gets called)
        poll_data = {'test': 'testing'}

        poll_created = datetime.datetime.now()

         # instert variables into the database
        sql = "INSERT INTO Polls VALUES (?, ?, ?, ?)"
        new_poll = (poll_id, user_id, poll_data, poll_created)
        
        #execute sql statement to insert the values contained in new poll.
        c.execute(sql, new_poll)
        conn.commit()
        conn.close()
        
    '''Renders an HTML template that allows users to create a poll'''
    return render_template("create_poll.html", name=name)

@app.route('/redirect_vote', methods=['GET'])
def redirect_vote():
    response = {'vote_url': url_for('take_a_poll')}
    return jsonify(response)

@app.route('/vote_test')
def vote_test():
        question = {"Who?":["You", "Me"], "Where?": ["Here", "There", "Everywhere"], "When?": ["Before", "After", "During", "Later"]}
        return render_template("vote.html", questions=question)

#Need to find way to access poll_id
@app.route('/vote', methods=['GET', 'POST'])
def take_a_poll(name=None, poll_id=111111111):

    conn = psycopg2.connect("postgres://pollaris_db_user:wzlXGhePudWAa8KTs0DKAzIRnoNVrEOp@dpg-clrjq9pjvg7s73ei8g0g-a/pollaris_db")
    c = conn.cursor()

    if poll_id==111111111:
        poll = {"Who?":["You", "Me"], "Where?": ["Here", "There", "Everywhere"], "When?": ["Before", "After", "During", "Later"]}
    else:
        c.execute('''SELECT poll_data FROM Polls WHERE poll_id="{}"'''.format(poll_id))
        poll = c.fetchone()[0]
        conn.close()

    if request.method == "POST":
        conn = psycopg2.connect("postgres://pollaris_db_user:wzlXGhePudWAa8KTs0DKAzIRnoNVrEOp@dpg-clrjq9pjvg7s73ei8g0g-a/pollaris_db")
        c = conn.cursor()
        c.execute('''SELECT user_id FROM Users WHERE username="{}"'''.format(session['username']))
        
        user_id = c.fetchone()[0]
        
        #Get javascript dict somehow and add it here.
        # CAT LOOK HERE - ajax call?
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
            c.execute("INSERT INTO Votes VALUES (?, ?, ?, ?, ?);", (vote))
            conn.commit()
        conn.close()

    '''Renders an HTML template that allows users to vote in an existing poll'''
    return render_template("voting_page.html", name=name, questions=poll)

@app.route('/popular')
def popular_polls(name=None):
    '''Renders an HTML template that displays popular, already-existing polls for users to browse and take'''
    return render_template("popular_polls.html", name=name)
