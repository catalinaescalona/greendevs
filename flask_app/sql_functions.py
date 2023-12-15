import sqlite3
import datetime
import requests
import json
from random import randint

def create_json_qs(questions):
    ''' 
    This function converts a python list of questions to a JSON-compatible string to be stored in the SQL database.
        
    Arguments: Python list that contains all questions for a given poll.
        
    Returns: String in a JSON format.
    '''
    
    # Creates a dictionary with key "questions" that contains the list of poll questions
    ques = {}
    ques['questions'] = questions
    
    # Convert dictionary to a string. 
    # The single quote char (') in the python dictionary must be converted to a double quote (")
    return str(ques).replace("'", '"')


def create_json_opts(options):
    ''' 
    This function converts a python list of response options to a JSON string to be uploaded to the SQL database.
        
    Arguments: Python list that contains all response options for a given poll.
        
    Returns: String in a JSON format.
    '''
    
    # Creates a dictionary with key "options" that contains the list of question response options.
    opts = {}
    opts['options'] = options
    
    # Convert dictionary to a string. 
    # The single quote char (') in the python dictionary must be converted to a double quote (")
    return str(opts).replace("'", '"')



def create_polls_db(): 
    conn = sqlite3.connect("db", timeout=10)
    c = conn.cursor()
    c.execute("DROP TABLE if EXISTS Polls;")

    c.execute('''
        CREATE TABLE Polls(
            poll_id INT, 
            user_id INT, 
            question JSON, 
            options JSON,
            poll_created VARCHAR(100),
            poll_expiration VARCHAR(60),
            poll_num INT,
            option_num INT,
            PRIMARY KEY (poll_id),
            FOREIGN KEY (user_id) REFERENCES Users(user_id)
        );
    ''')
    
    # Option num may need to be removed and just have a function that tallies from the votes table 
    # using the question num and poll num
    
    # Poll_num may need to be removed and just have a function that tallies numbers of users that have taken a poll

    polls = [(111111111, 100000000, json_questions, json_options, '1/1/2023', '1/1/2024', 111, 'option_num1'), 
             (222222222, 200000000, json_questions, json_options, '2/2/2023', '2/2/2024', 222, 'option_num2'),
             (333333333, 300000000, json_questions, json_options, '3/3/2023', '3/3/2024', 333, 'option_num3')]

    for poll in polls:
        poll_id, user_id, question, options, poll_created, poll_expiration, poll_num, option_num = poll
        c.execute("INSERT INTO Polls VALUES (?, ?, ?, ?, ?, ?, ?, ?);", poll)
    conn.commit()

    a = c.execute('''SELECT * FROM Polls;''')
    for poll in a.fetchall():
        print(poll)

    conn.close()


def create_users_db():
    conn = sqlite3.connect("db", timeout=10)
    c = conn.cursor()
    c.execute("DROP TABLE if EXISTS Users")

    c.execute('''CREATE TABLE Users(user_id INT NOT NULL, 
                                    user_name VARCHAR(30), 
                                    first_name VARCHAR(50), 
                                    last_name VARCHAR(50),
                                    email VARCHAR(100) NOT NULL,
                                    password VARCHAR(60) NOT NULL,
                                    member_since VARCHAR(60),
                                    
                                    PRIMARY KEY (user_id)
             );''')

    users = [(100000000, 'username1', 'First1', 'Last1', 'teme1111@colorado.edu', '111111', '11-01-2022'), 
             (200000000, 'username2', 'First2', 'Last2', 'teme2222@colorado.edu', '222222', '12-02-2022'),
             (300000000, 'username3', 'First3', 'Last3', 'teme3333@colorado.edu', '333333', '01-03-2023')]

    for user in users:
        user_id, user_name, first_name, last_name, email, password, member_since = user
        c.execute("INSERT INTO Users VALUES (?, ?, ?, ?, ?, ?, ?);", user)
    conn.commit()

    a = c.execute('''SELECT * FROM Users;''')
    for user in a.fetchall():
        print(user)

    conn.close()
 
    
def create_votes_db(): 
    conn = sqlite3.connect("db", timeout=10)
    c = conn.cursor()
    c.execute("DROP TABLE if EXISTS Votes")

    c.execute('''CREATE TABLE Votes(vote_id INT,
                                    user_id INT,
                                    poll_id INT,
                                    question_id INT,
                                    option_id INT,
                                    vote_created VARCHAR(45),
                                    ip_address VARCHAR(45),
                                    is_anon BOOLEAN,
                                    
                                    PRIMARY KEY (vote_id),
                                    FOREIGN KEY (user_id) REFERENCES Users(user_id),
                                    FOREIGN KEY (poll_id) REFERENCES Polls(poll_id)
             );''')

    votes = [(111111111, 100000000, 111000111, 1, 1, '1-1-2023', "1.01.011.1111", '1'), 
             (222222222, 200000000, 222000222, 2, 2, '2-2-2023', "2.02.022.2222", '0'), 
             (333333333, 300000000, 333000333, 3, 3, '3-3-2023', "3.03.033.3333", '0')]

    for vote in votes:
        vote_id, user_id, poll_id, question_id, option_id, vote_created, ip_address, is_anon = vote
        c.execute("INSERT INTO Votes VALUES (?, ?, ?, ?, ?, ?, ?, ?);", (vote))
    conn.commit()

    a = c.execute('''SELECT * FROM Votes;''')
    for i in a:
        print(i)

    conn.close()
    
def add_poll(user_id, questions, options):
    '''
    This function adds a newly created poll to the Pollaris database.
    
    Arugments:  user_id (integer)
                List of questions
                2D list containing lists of question options for each question.
                Poll expiration date
                
    Returns nothing.      
    '''
    
    # Connect to database
    conn = sqlite3.connect("db", timeout=10)
    c = conn.cursor()
    
    # poll_id must be unique! 
    # Create a random 9 digit integer. Search database to determine if the id already exists.
    new_id = randint(100000000, 999999999)
    result = c.execute("SELECT * FROM Polls WHERE poll_id='{}'".format(new_id))
    
    # If poll_id exists, continue to pick a new poll_id until one is picked that does not exist in the database.
    if result.fetchone() != None:
        while result.fetchone() != None:
            new_id = randint(100000000, 999999999)
            result = c.execute("SELECT * FROM Polls WHERE poll_id='{}'".format(new_id))
    
    # Just adding dummy data for testing -- will be removed
    json_qs = create_json_qs(questions)
    json_as = create_json_opts(options)
    
    # Set variables --- Some hard-coded b/c need to determine inputs from javascript, etc.
    poll_id = new_id
    user_id = user_id
    question = json_qs
    options = json_as
    poll_created = datetime.datetime.now()
    poll_expiration = "1-1-2024"
    poll_num = 0
    option_num = 0
    
    
    # instert variables into the database
    sql = "INSERT INTO Polls VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    new_poll = (poll_id, user_id, question, options, poll_created, poll_expiration, poll_num, option_num)
    
    #execute sql statement to insert the values contained in new poll.
    c.execute(sql, new_poll)
    
    #print data ------ will be removed
    sql1 = "SELECT * FROM Polls"
    c.execute(sql1)
    for i in c.fetchall():
        print(i)
    
    #commit changes and close database.
    conn.commit()
    conn.close()


def create_account():
    ############ Need to add Length requirement for inputs and regex for valid chars (first, last, email, etc.)
    '''
    This function adds a new user to the database
    
    Arguments: first name, last name, username, email, and password
    
    Returns nothing.
    '''
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
    
    # username must be unique!
    # Check if username exists. If it does, request new name until unused name chosen.
    # Replace python input with GET request from javascript.
    username = input("Enter your user name: ")
    new_name = c.execute("SELECT * FROM Users WHERE user_name='{}'".format(username)).fetchone()

    # Continue to get username until one is entered that is not taken.
    if new_name != None:
        while new_name != None:
            username = input("User name taken. Please try again: ")
            new_name = c.execute("SELECT * FROM Users WHERE user_name='{}'".format(username)).fetchone()

    user_id = new_id
    username = username
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    timestamp = datetime.datetime.now()
    
    #insert values into table
    sql = "INSERT INTO Users VALUES (?, ?, ?, ?, ?, ?, ?)"
    new_user = (user_id, username, first, last, email, password, timestamp)
    c.execute(sql, new_user)
    
    # Print statement to be removed once implemented into app
    for i in c.execute("SELECT * FROM Users").fetchall(): 
        print(i)
    
    # Commit changes and close database
    conn.commit()
    conn.close()

def check_login_credentials():
    '''
    This function checks log in credentials when a user attempts to log in.
    
    Arguments: 2 GET request from javascript that contain username and password.
    
    Returns: String indicating whether log in succeeded or failed -- may remove once implemented.
    '''
    
    # Connect to databse
    conn = sqlite3.connect("db", timeout=10)
    c = conn.cursor()
    
    # Get input from user --- python input statements will need to be replaced with GET requests
    username = input("Please enter your user name: ")
    password = input("Please enter your password: ")
    
    # Create string to query database. Gets
    login_query = '''SELECT user_name, password FROM Users WHERE user_name="{}" AND password="{}";'''.format(username, password)

    # Execute sql query to get data where username and password match user input
    c.execute(login_query)

    # If the credentials don't match, the fetchone() function will return nothing.
    # Execute log in if fetchone() returns valid user
    if not c.fetchone():
        return "Login failed. Please try again."
    else:
        return "login success!"
    
    # Close database
    conn.close()
    
    
def get_questions(poll_id):
    '''
    This function retrieves all questions for a given poll.
    
    Arguments: a valid poll_id
    
    Returns: A python list containing all question options.
    '''
    # Connect to databes
    conn = sqlite3.connect("db", timeout=10)
    c = conn.cursor()

    # Query database for all questions for a given poll id.
    a = c.execute("SELECT json_extract(question, '$.questions') FROM Polls WHERE poll_id='{}'".format(poll_id))
    
    # a.fetchone() returns a tuple. The questions data is stored in the first position ([0]).
    # use the json.loads to convert the data from a string to a list.
    list_of_questions = json.loads(a.fetchone()[0])

    conn.close()
    
    return list_of_questions   
    
def get_options(poll_id):
    '''
    This function retrieves all question options for a given poll.
    
    Arguments: a valid poll_id.
    
    Returns: A python list containing python lists for each question's response options.
    '''
    
    # Connect to database
    conn = sqlite3.connect("db", timeout=10)
    c = conn.cursor()

    # Query to retrieve the JSON options for the given poll_id
    a = c.execute("SELECT json_extract(options, '$.options') FROM Polls WHERE poll_id='{}'".format(poll_id))
    
    # a.fetchone() returns a tuple. The options data is stored in the first position ([0]).
    # use the json.loads to convert the data from a string to a list of lists
    list_of_options = json.loads(a.fetchone()[0])
    
    # Close database
    conn.close()
    
    return list_of_options   
    
    
    
####################################################################################################    
    
    
    # TESTING
    
####################################################################################################  
    
# Data to use for testing
questions = ["What class is this?", "What is our team name?", "What is our project name?"]

options = [["CSPB 1300", "CSPB 3308", "CSPB 2270", "CSPB 2824", "CSPB 3104", "CSPB 4444"],
             ["green", "greendevs", "devs"], 
             ["Pollaris", "Make Polls", "POLL MAKER", "Polling Place"]]

json_questions = create_json_qs(questions)
print(json_questions)

json_options = create_json_opts(options)
print(json_options)

# Create databases using hard-coded data within functions
create_users_db()
create_polls_db()
create_votes_db()

# Enter data to create an account
create_account()

# Log in using account info
check_login_credentials()

# Add a poll by adding user_id, questions list, and options list
user_id = 100000000
add_poll(user_id, questions, options)

# Poll id to test JSON
poll_id = 111111111

qs = get_questions(poll_id)

print("Poll ID: ", poll_id)
print("Questions: ", '\n----------')
for i in range(len(qs)):
    print("question", i+1, ": ", qs[i])

options = get_options(poll_id)
print("Poll ID: ", poll_id)
print("Options", '\n--------')
for i in range(len(options)):
    print("question", i+1, ": ", options[i])
    
opts = ['a', 'b', 'c', 'd', 'e', 'f']
for i in range(len(qs)):
    print(str(i+1)+'.', qs[i], '\n------------------------')
    for j in range(len(options[i])):
        print(str(opts[j])+'.', options[i][j])
    print("\n")

