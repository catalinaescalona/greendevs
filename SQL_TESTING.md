# Pollaris - Project Tables and Tests

## <ins>Table #1</ins>

### Table Name: 

Polls Table

### Description:

This table stores individual poll information.

### Table Fields:

* poll_id - primary key
* user_id - foreign key to Users Table
* question - text questions
* options - JSON column to store options as arrays
* poll_created - poll creation timestamp
* poll_expiration - poll expiration date

### Table verification tests

* Poll creation test
* Poll update test
* Poll deletion test
* Foreign key validity test
* Data accuracy test

### Data access test pre-conditions:

* The user is logged in.
* A connection to the database is established.

### Test steps:

* Create a new poll and enter it into the Polls Table.
* Retrieve the new poll from the Polls Table using an SQL query.

### Expected result:

* Entering the new poll into the Polls Table works without errors.
* The SQL query retrieves the correct new poll from the Polls Table.

### Actual result:

* The new poll is entered into the Polls Table successfully.
* The SQL query retrieves the correct new poll from the Polls Table.

### Status:

Pass

### Notes:

This test confirms that new polls are correctly entered into and retrieved from the Polls Table.

### Post-conditions:

* The new poll is contained within the Polls Table.
* The website correctly displays the poll to users.

<br></br>



## <ins>Table #2</ins>

### Table Name: 

Votes Table

### Description:

This table stores poll votes by users.

### Table Fields:

* vote_id - primary key
* user_id - foreign key to Users Table
* poll_id - foreign key to Polls Table
* option_id - selected options 
* vote_created - vote timestamp

### Table verification tests

* Vote recording test
* Multiple votes test
* Data accuracy test

### Data access test pre-conditions:

* The user is logged in.
* A connection to the database is established.

### Test steps:

* Cast a vote and enter it into the Votes Table.
* Retrieve the vote from the Votes Table using an SQL query.

### Expected result:

* Casting a vote and entering it into the Votes Table works without errors.
* The SQL query retrieves the correct vote from the Votes Table.

### Actual result:

* The vote is entered into the Votes Table successfully.
* The SQL query retrieves the correct vote from the Votes Table.

### Status:

Pass

### Notes:

This test confirms that new votes are correctly entered into and retrieved from the Votes Table.

### Post-conditions:

* The vote is contained within the Votes Table and is linked to the correct poll.
* The vote is added to the total number of votes collected for a specific poll.

<br></br>



## <ins>Table #3</ins>

### Table Name: 

Users Table

### Description:

This table stores individual user information.

### Table Fields:

* user_id - primary key
* username - login id for user authentication
* email - user email address
* password - user password
* user_created - vote timestamp

### Table verification tests

* User registration test
* User authentication test
* Username/email validity test
* Password hashing test

### Data access test pre-conditions:

* The website and data are functional and properly configured.
* A connection to the database is established.

### Test steps:

* Create a new user and enter it into the Users Table.
* Retrieve the new user from the Users Table using an SQL query.

### Expected result:

* Entering the new user into the Users Table works without errors.
* The SQL query retrieves the correct new user from the Users Table.

### Actual result:

* The new user is entered into the Users Table successfully.
* The SQL query retrieves the correct new user from the Users Table.

### Status:

Pass

### Notes:

This test confirms that new users are correctly entered into and retrieved from the Users Table.

### Post-conditions:

* The new user is contained within the Users Table.
* The new user is successfully registered in the system.

