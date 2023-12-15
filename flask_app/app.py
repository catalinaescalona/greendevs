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
app.secret_key = "Pollaris"
    
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
        c.execute('''CREATE TABLE IF NOT EXISTS Users(user_id INT, 
                                                      user_name VARCHAR(30), 
                                                      first_name VARCHAR(50), 
                                                      last_name VARCHAR(50),
                                                      email VARCHAR(100),
                                                      password VARCHAR(60),
                                                      member_since VARCHAR(60)
                 );''')
    
        c.execute('''CREATE TABLE IF NOT EXISTS Polls(poll_id INT,
                                                      user_id INT,
                                                      poll_data JSON,
                                                      poll_created VARCHAR(45)
                );''')             
        
        c.execute('''CREATE TABLE IF NOT EXISTS Votes(vote_id INT,
                                                      user_id INT,
                                                      poll_id INT,
                                                      question_id INT,
                                                      option_id INT,
                                                      vote_created VARCHAR(45)
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

        username = request.form['username']
        password = request.form['password']

        if username != "" and password != "":
            # Create string to query database for login credentials and execute query
            login_query = 'SELECT * FROM Users WHERE user_name=%s AND password=%s;'
            c.execute(login_query, (username, password))
            result = c.fetchone()

        else:
            result = None

        # If the credentials don't match, the result=c.fetchone() function will return nothing.
        if result == None:
            # display log in error message
                        
            # Close database
            conn.close()
            return render_template('login_page.html')
        else:
            #redirect to user/<user_name>
                        
            # Close database
            conn.close()
            session["username"] = username
            return redirect(url_for('create_poll'))
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
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'first' in request.form and 'last' in request.form:

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
        c.execute("SELECT * FROM Users WHERE user_id='{}';".format(new_id))
        result = c.fetchone()
        
        # c.execute will return nothing if the id does not exist.
        #If user_id already exists, randomly select new 9-digit id until one is chose that does not exist already.
        if result != None:
            while result != None:
                new_id = randint(100000000, 999999999)
                c.execute("SELECT * FROM Users WHERE user_id='{}';".format(new_id))
                result = c.fetchone()

        # user_name must be unique. return error message indicating user name is taken if not unique
        c.execute("SELECT * FROM Users WHERE user_name='{}';".format(user_name))
        new_name = c.fetchone()
        if new_name != None:
            conn.close()
            return render_template('sign_up.html')
        # Chech regex match to verify valid email address.
        if not re.match(r'^[A-Za-z\.!#$%\*0-9]+@[A-Za-z0-9]+\.[a-zA-Z]{2,3}$', email):
            conn.close()
            return render_template('sign_up.html')
        # email must be unique. return error message if email is associated with an account
        c.execute("SELECT * FROM Users WHERE user_name='{}';".format(email))
        new_email = c.fetchone()
        if new_email != None:
            conn.close()
            return render_template('sign_up.html')
        
        timestamp = datetime.datetime.now()

        cols = "(user_id, user_name, first_name, last_name, email, password, member_since)"
        sql = "INSERT INTO Users " + cols + " VALUES (%s, %s, %s, %s, %s, %s, %s)"
        #insert values into table
        new_user = (new_id, user_name, first, last, email, password, timestamp)
        c.execute(sql, new_user)
        
        # Commit changes
        conn.commit()

        # Set the session variable with the username
        session["username"] = user_name

        # Close database
        conn.close()

        # Redirect to create a poll page CHANGED
        # return redirect(url_for("create_poll"))
        # return redirect(url_for("user_page", user_name=user_name))
        return redirect(url_for("log_in"))
    else:
        return render_template('sign_up.html')
    #return render_template('sign_up.html')

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
@app.route('/create_test', methods=["GET", "POST"])
def create_poll_test(name=None):
    if request.method == 'POST':
        poll_data = request.get_json()
        return "<h1> Got post </h1>"
    return render_template("create_poll.html", name=name)
    
@app.route('/create', methods=["GET", "POST"])
def create_poll(name=None):
    
    if request.method=="POST":
        conn = psycopg2.connect("postgres:/pollaris_db_user:wzlXGhePudWAa8KTs0DKAzIRnoNVrEOp@dpg-clrjq9pjvg7s73ei8g0g-a/pollaris_db")
        c = conn.cursor()

        c.execute('''SELECT user_id FROM Users WHERE username="{}";'''.format(session['username']))
        user_id = c.fetchone()[0]
        
        poll_id = randint(100000000, 999999999)
        result = c.execute("SELECT * FROM Users WHERE user_id='{}';".format(new_id))
        
        # c.execute will return nothing if the id does not exist.
        # If user_id already exists, randomly select new 9-digit id until one is chose that does not exist already.
        if result != None:
            while result != None:
                poll_id = randint(100000000, 999999999)
                result = c.execute("SELECT * FROM Users WHERE user_id='{}';".format(new_id))
        
        #NEED TO GET THIS FROM JAVASCRIPT (test dictionary, but fill in with what gets called)
        poll_data = {"test": "testing"}

        poll_created = datetime.datetime.now()

         # instert variables into the database
        sql = "INSERT INTO Polls VALUES (?, ?, ?, ?);"
        new_poll = (poll_id, user_id, poll_data, poll_created)
        
        #execute sql statement to insert the values contained in new poll.
        c.execute(sql, new_poll)
        conn.commit()
        conn.close()

        # Redirect to take_a_poll page with the newly created poll_id CHANGED
        return redirect(url_for("take_a_poll", poll_id=poll_id))
        
    '''Renders an HTML template that allows users to create a poll'''
    return render_template("create_poll.html", name=name)

@app.route('/redirect_vote', methods=['GET'])
def redirect_vote():
    response = {'vote_url': url_for('take_a_poll')}
    return jsonify(response)

@app.route('/vote_test')
def vote_test():
        question = {"Presentation Poll":["option 1", "option 2", "option 3"]}
        return render_template("vote.html", questions=question)

@app.route('/vote', methods=['GET', 'POST'])
def take_a_poll(name=None, poll_id=111111111):

    conn = psycopg2.connect("postgres://pollaris_db_user:wzlXGhePudWAa8KTs0DKAzIRnoNVrEOp@dpg-clrjq9pjvg7s73ei8g0g-a/pollaris_db")
    c = conn.cursor()

    if poll_id==111111111:
        poll = {"Presentation Poll":["good", "great", "amazing"]}
    else:
        c.execute('''SELECT poll_data FROM Polls WHERE poll_id="{}";'''.format(poll_id))
        poll = c.fetchone()[0]
        conn.close()

    if request.method == "POST":
        conn = psycopg2.connect("postgres://pollaris_db_user:wzlXGhePudWAa8KTs0DKAzIRnoNVrEOp@dpg-clrjq9pjvg7s73ei8g0g-a/pollaris_db")
        c = conn.cursor()
        c.execute('''SELECT user_id FROM Users WHERE username="{}";'''.format(session['username']))
        
        user_id = c.fetchone()[0]
        
        #Get javascript dict somehow and add it here.
        # CAT LOOK HERE - ajax call?
        responses = request.form["answers"]
        
        for q_no, answer in responses:
            new_id = randint(100000000, 999999999)
            result = c.execute("SELECT * FROM Users WHERE user_id='{}';".format(new_id))
            
            # c.execute will return nothing if the id does not exist.
            # If user_id already exists, randomly select new 9-digit id until one is chose that does not exist already.
            if result != None:
                while result != None:
                    new_id = randint(100000000, 999999999)
                    result = c.execute("SELECT * FROM Users WHERE user_id='{}';".format(new_id))
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


