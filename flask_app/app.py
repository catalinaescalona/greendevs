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
from urllib.parse import urlparse
import datetime
import psycopg2
import re
import json
import uuid 

app = Flask(__name__)
app.secret_key = "Pollaris"

# Function to establish a database connection using the provided URL
def connect_to_database():
    url = urlparse("postgres://pollaris_db_user:wzlXGhePudWAa8KTs0DKAzIRnoNVrEOp@dpg-clrjq9pjvg7s73ei8g0g-a/pollaris_db")
    db_params = {
        'dbname': url.path[1:],
        'user': url.username,
        'password': url.password,
        'host': url.hostname,
        'port': url.port
    }
    return psycopg2.connect(**db_params)

# Function to generate a unique poll_id (you can use a library like uuid)
def generate_unique_poll_id(c):
    #poll_id = str(uuid.uuid4())
    poll_id = randint(100000000, 999999999)

    # Check if the generated poll_id already exists in the database
    while True:
        c.execute("SELECT * FROM Polls WHERE poll_id = %s;", (poll_id,))
        existing_poll = c.fetchone()
        if not existing_poll:
            break
        #poll_id = str(uuid.uuid4())
        poll_id = randint(100000000, 999999999)

    return poll_id

# Function to get the user_id of the current user by username
def get_user_id_by_username(username, c):
    c.execute("SELECT user_id FROM Users WHERE user_name = %s;", (username,))
    user_id = c.fetchone()
    if user_id:
        return user_id[0]
    else:
        return None

# Function to save the poll data to the database
def save_poll_to_database(c, poll_id, user_id, question, options):
    # Create a JSON object to store poll data (question and options)
    poll_data = {
        'question': question,
        'options': options
    }

    # Get the current timestamp
    poll_created = datetime.datetime.now()

    # Insert the new poll into the database
    c.execute(
        'INSERT INTO Polls (poll_id, user_id, poll_data, poll_created) VALUES (%s, %s, %s, %s)',
        (poll_id, user_id, json.dumps(poll_data), poll_created)
    )

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

@app.route('/', methods=["GET", "POST"])
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
    
    if request.method == "POST":
        poll = request.form['pollid']
        return redirect(url_for("take_a_poll", poll_id=int(poll)))
    
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
def log_in():
    '''
    This function checks login credentials when a user attempts to log in.
    It queries the database for the credentials.
    If credentials exist, the user is redirected to their profile page. Otherwise, a login error message is displayed.
    '''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Connect to the database
        conn = connect_to_database()
        c = conn.cursor()

        username = request.form['username']
        password = request.form['password']

        if username != "" and password != "":
            # Create a string to query the database for login credentials and execute the query
            login_query = 'SELECT * FROM Users WHERE user_name=%s AND password=%s;'
            c.execute(login_query, (username, password))
            result = c.fetchone()
        else:
            result = None

        # If the credentials don't match, the result=c.fetchone() function will return nothing.
        if result is None:
            # Display a login error message
            # Close the database
            conn.close()
            return render_template('login_page.html')
        else:
            # Redirect to the user's profile page
            # Close the database
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

        # Connect to the database
        conn = connect_to_database()
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
        c.execute("SELECT * FROM Users WHERE user_id=%s;", (new_id,))
        result = c.fetchone()
        
        # c.execute will return nothing if the id does not exist.
        # If user_id already exists, randomly select new 9-digit id until one is chosen that does not exist already.
        if result is not None:
            while result is not None:
                new_id = randint(100000000, 999999999)
                c.execute("SELECT * FROM Users WHERE user_id=%s;", (new_id,))
                result = c.fetchone()

        # user_name must be unique. Return error message indicating username is taken if not unique.
        c.execute("SELECT * FROM Users WHERE user_name=%s;", (user_name,))
        new_name = c.fetchone()
        if new_name is not None:
            conn.close()
            return render_template('sign_up.html')
        
        # Check regex match to verify a valid email address.
        if not re.match(r'^[A-Za-z\.!#$%\*0-9]+@[A-Za-z0-9]+\.[a-zA-Z]{2,3}$', email):
            conn.close()
            return render_template('sign_up.html')
        
        # Email must be unique. Return an error message if the email is associated with an account.
        c.execute("SELECT * FROM Users WHERE email=%s;", (email,))
        new_email = c.fetchone()
        if new_email is not None:
            conn.close()
            return render_template('sign_up.html')
        
        timestamp = datetime.datetime.now()

        cols = "(user_id, user_name, first_name, last_name, email, password, member_since)"
        sql = "INSERT INTO Users " + cols + " VALUES (%s, %s, %s, %s, %s, %s, %s)"
        # Insert values into the table
        new_user = (new_id, user_name, first, last, email, password, timestamp)
        c.execute(sql, new_user)
        
        # Commit changes
        conn.commit()

        # Set the session variable with the username
        session["username"] = user_name

        # Close the database
        conn.close()

        # Redirect to the login page
        return redirect(url_for("log_in"))
    else:
        return render_template('sign_up.html')

# @app.route('/user/<user_name>')
# def user_page(user_name):
#     '''Temporary function that will eventually render an HTML template that displays user's profile page'''
#     message = "<h1>"
#     message += str(user_name)
#     message += "</h1>"
#     return message

#testing new dynamic form
# @app.route('/create_testing', methods=["GET", "POST"])
# def create_testing():
#     if request.method == "POST":
#         dict = {}
#         questions = request.form.getlist('question')
#         for i in range(len(questions)):
#             q = str(questions[i])
#             opts = request.form.getlist('option'+str(i)) 
#             dict[q] = opts

#         conn = connect_to_database()
#         c = conn.cursor()

#         # Get the user_id of the current user
#         user_id = get_user_id_by_username(session['username'], c)

#         # Generate a unique poll_id
#         poll_id = generate_unique_poll_id(c)

#         poll_created = datetime.datetime.now()

#         json = str(dict).replace("'", '"')

#         c.execute('INSERT INTO Polls (poll_id, user_id, poll_data, poll_created) VALUES (%s, %s, %s, %s)',
#          (poll_id, user_id, json, poll_created))

#         conn.commit()
#         conn.close()

#         return "<p>"+str(poll_id)+"</p><br>"+"<p>"+str(user_id)+"</p><br>"+"<p>"+str(dict)+"</p><br>"+"<p>"+str(poll_created)+"</p>"
#     else:
#         return render_template("create_test.html")


# GET AJAX METHOD TO WORK HERE
# @app.route('/create_test', methods=["GET", "POST"])
# def create_poll_test(name=None):
#     if request.method == 'POST':
#         poll_data = request.get_json()
#         response = {'message': 'Data Sent Successfully!'}
#         return jsonify(response)
#     return render_template("create_poll.html", name=name)

# Existing route for rendering the create poll page with a GET request
# @app.route('/create', methods=["GET"])
# def render_create_poll():
#     return render_template("create_poll.html")

@app.route('/redirect_create', methods=['GET'])
def redirect_create():
    response = {'create_url': url_for('create_poll')}
    return jsonify(response)

@app.route('/create', methods=["GET", "POST"])
def create_poll():
    if request.method == "POST":
        dict = {}
        questions = request.form.getlist('question')
        for i in range(len(questions)):
            q = str(questions[i])
            opts = request.form.getlist('option'+str(i)) 
            dict[q] = opts

        conn = connect_to_database()
        c = conn.cursor()

        # Get the user_id of the current user
        user_id = get_user_id_by_username(session['username'], c)

        # Generate a unique poll_id
        poll_id = generate_unique_poll_id(c)

        poll_created = datetime.datetime.now()

        json = str(dict).replace("'", '"')

        c.execute('INSERT INTO Polls (poll_id, user_id, poll_data, poll_created) VALUES (%s, %s, %s, %s)',
         (poll_id, user_id, json, poll_created))

        conn.commit()
        conn.close()

        return "<p> Poll ID: "+str(poll_id)+"</p><br>"+"<p> User ID: "+str(user_id)+"</p><br>"+"<p> Data: "+str(dict)+"</p><br>"+"<p> Timestamp: "+str(poll_created)+"</p>"
    else:
        return render_template("create_test.html")





    
    # if request.method == "POST":
    #     # Connect to the database
    #     conn = connect_to_database()
    #     c = conn.cursor()

    #     # Get the user_id of the current user
    #     user_id = get_user_id_by_username(session['username'], c)

    #     # Generate a unique poll_id
    #     poll_id = generate_unique_poll_id(c)

    #     # Extract poll data from the form (you may need to modify this based on your form fields)
    #     question = request.form.get('question')
    #     options = request.form.getlist('option')

    #     # Save the poll data to the database
    #     save_poll_to_database(c, poll_id, user_id, question, options)

    #     # Close the database connection
    #     conn.close()

    #     # Redirect to the voting page with the newly created poll_id
    #     return redirect(url_for("take_a_poll", poll_id=poll_id))  # Updated redirection

    # # Renders an HTML template that allows users to create a poll
    # return render_template("create_poll.html")



#THIS WORKS AND WE NEED TO IMPLEMENT WITHIN THE TAKE POLL ROUTE
# @app.route('/vote_test/<poll_id>', methods=["GET", "POST"])
# def vote_test(poll_id):

#     # Connect to the database
#     conn = connect_to_database()
#     c = conn.cursor()

#     try:
#         c.execute("SELECT poll_data FROM Polls WHERE poll_id=%s", (poll_id,))
#         poll = c.fetchone()[0]
#         conn.close()
        
#         return render_template("voting_page.html", questions=poll)
#     except:
#         conn.close()
#         return "<h1>Invalid Poll ID</h1>"
    

@app.route('/redirect_vote', methods=['GET'])
def redirect_vote():
    response = {'vote_url': url_for('take_a_poll')}
    return jsonify(response)
    
@app.route('/take_poll/<poll_id>', methods=['GET', 'POST'])
def take_a_poll(poll_id):

    # Connect to the database
    conn = connect_to_database()
    c = conn.cursor()

    try:
        c.execute("SELECT poll_data FROM Polls WHERE poll_id=%s", (poll_id,))
        poll = c.fetchone()[0]
        conn.close()

        if request.method == "POST":
            # Connect to the database
            conn = connect_to_database()
            c = conn.cursor()
    
            # Get the user_id of the current user
            user_id = get_user_id_by_username(session['username'], c)
    
            # Get poll option data
            options = []

            questions = list(poll)
            answers = list(poll.values())
            for i in range(len(questions)):
                opt_name = "option"+str(i+1)
                ans = request.form.getlist(opt_name)
                options.append(ans[0])

            html_txt = "<h1>Thank you for voting! The following options were recorded:</h1><br>"
            for i in range(len(questions)):
                o_no = int(options[0])
                html_txt += "<h3>"+str(i+1)+". "+str(questions[i])+"</h3><br>"
                for j in answers[i]:
                    if j == o_no:
                        html_txt += "<b>"+str(o_no+1)+". "+str(answers[i][o_no])+"</b><br>"
                    else:
                        html_txt += "<p>"+str(o_no+1)+". "+str(answers[i][o_no])+"</p><br>"
                
            return html_txt
            

        # # Iterate over the received data and insert votes into the database
        # for question_id, option_id in data.items():
        #     vote_created = datetime.datetime.now()
        #     c.execute('INSERT INTO Votes (user_id, poll_id, question_id, option_id, vote_created) VALUES (%s, %s, %s, %s, %s)',
        #               (user_id, poll_id, question_id, option_id, vote_created))
        #     conn.commit()

        # # Close the database connection
        # conn.close()

        # # Render an HTML template that allows users to vote in an existing poll
        # return render_template("voting_page.html", name=session['username'], questions=poll)
        
        return render_template("voting_page.html", questions=poll)
    except:
        conn.close()
        return "<h1>Invalid Poll ID</h1>"

    


# @app.route('/popular')
# def popular_polls(name=None):
#     '''Renders an HTML template that displays popular, already-existing polls for users to browse and take'''
#     return render_template("popular_polls.html")

if __name__ == '__main__':
    app.run(debug=True)

