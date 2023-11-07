# Pollaris - Project Tables and Tests


## <ins>Table #1</ins>

### Table Name: 

Users

### Description:

This table stores individual user information.

### Table Fields:

* user_id - int identity [primary key], unique user ID
* username - varchar(30), username created by user
* first_name - varchar(50), first name of user
* last_name - varchar(50), last name of user
* email - varchar(100), user's email address
* password - varchar(60), password created by user
* user_created - timestamp, time when user profile was created

### Table verification tests

* User registration test
* Username/email validity test
* Password hashing test

### Data access test pre-conditions:

* The website and database are functional and properly configured.
* A connection to the database is established.

### Test steps:

* User registration test
  * Create a new user and enter it into the Users Table.
  * Retrieve the new user from the Users Table using an SQL query.
* Username/email validity test
  * Attempt to register a user that already exists in the database.
  * Confirm the system prevents duplicate user registration.
* Password hashing test
  * Create a new user with password and enter it into the Users Table.
  * Retrieve the hashed password from the Users Table using an SQL query and confirm validity.

### Expected result:

* User registration test
  * Entering the new user into the Users Table works without errors.
  * The SQL query retrieves the correct new user from the Users Table.
* Username/email validity test
  * The website prevents registration if username or password is not unique.
* Password hashing test
  * The stored password matches the newly hashed password.

### Actual result:

* User registration test
  * The new user is entered into the Users Table successfully.
  * The SQL query retrieves the correct new user from the Users Table.
* Username/email validity test
  * The website prevents registration if username or email address is not unique.
* Password hashing test
  * The stored password matches the newly hashed password.

### Status:

Pass

### Notes:

These tests confirm the following:
  * new users are correctly entered into and retrieved from the Users Table.
  * new users are registered with a unique username and email address.
  * new users passwords are stored accurately in the database.

### Post-conditions:

* The new user is contained within the Users Table.
* The new user is successfully registered in the system.
* The new user's password is stored correctly.

<br></br>


## <ins>Table #2</ins>

### Table Name: 

Polls

### Description:

This table stores individual poll information.

### Table Fields:

* poll_id - int identity [primary key], poll ID unique for each poll
* user_id - int identity [foreign key], ID of user who created poll
* question - text, stores the poll questions 
* options - JSON, stores the answer options of the poll questions
* poll_created - timestamp, time when poll was created
* poll_expiration - timestamp, time when poll expires
* poll_num - int, number of users who have taken that poll
* option_num - int, number of times a user selected a specific response option

### Table verification tests

* Poll creation test
* Poll update test
* Poll deletion test
* Foreign key validity test

### Data access test pre-conditions:

* The user is logged in.
* A connection to the database is established.

### Test steps:

* Poll creation test
  * Create a new poll and enter it into the Polls Table.
  * Retrieve the new poll from the Polls Table using an SQL query.
* Poll update test
  * Update existing poll and with new data in the Polls Table.
  * Confirm the accuracy of new data in the Polls Table.
* Poll deletion test
  * Delete an existing poll from the Polls Table.
  * Confirm the removal of existing poll from the Polls Table.
* Foreign key validity test
  * Verify the user_id in the Polls Table references a valid user_id in the Users Table.

### Expected result:

* Poll creation test
  * Entering the new poll into the Polls Table works without errors.
  * The SQL query retrieves the correct new poll from the Polls Table.
* Poll update test
  * Updating an existing poll in the Polls Table works without errors.
  * The updated poll data is reflected in the Polls Table.
* Poll deletion test
  * Delete an existing poll from the Polls Table works without errors.
  * Confirm the poll is removed from the Polls Table.
* Foreign key validity test
  * The user_id in the Polls Table references a valid user_id in the Users Table.

### Actual result:

* Poll creation test
  * The new poll is entered into the Polls Table successfully.
  * The SQL query retrieves the correct new poll from the Polls Table.
* Poll update test
  * The existing poll in the Polls Table is updated successfully.
  * The updated poll data is reflected in the Polls Table.
* Poll deletion test
  * The existing poll in the Polls Table is deleted successfully.
  * The poll is removed from the Polls Table.
* Foreign key validity test
  * The user_id in the Polls Table references a valid user_id in the Users Table.

### Status:

Pass

### Notes:

These tests confirm the following:
  * new polls are correctly entered into and retrieved from the Polls Table.
  * poll updates are reflected accurately in the Polls Table.
  * poll deletions are performed successfully on the Polls Table.
  * A valid user_id is referenced for each poll in the Polls Table.

### Post-conditions:

* New polls are created, updated, or deleted and accurately reflected in the Polls Table.
* The website correctly displays the poll to users.

<br></br>



## <ins>Table #3</ins>

### Table Name: 

Votes

### Description:

This table stores votes by users.

### Table Fields:

* vote_id - primary key (one user_id and poll_id per vote)
* user_id - foreign key to Users Table 
* poll_id - foreign key to Polls Table
* option_id - selected options 
* vote_created - vote timestamp

### Table verification tests

* Vote recording test
* Multiple votes test
* Foreign key validity test

### Test pre-conditions:

* The user is logged in.
* A connection to the database is established.

### Test steps:

* Vote recording test
   * Cast a vote and enter it into the Votes Table.
   * Retrieve the vote from the Votes Table using an SQL query.
* Multiple votes test
   * Attempt to cast multiple votes for the same user and poll.
   * Confirm the system prevents duplicate votes.
* Foreign key validity test
  * Verify the user_id in the Votes Table references a valid user_id in the Users Table.
  * Verify the poll_id in the Votes Table references a valid poll_id in the Polls Table.

### Expected result:

* Vote recording test
   * Casting a vote and entering it into the Votes Table works without errors.
   * The SQL query retrieves the correct vote from the Votes Table.
* Multiple votes test
   * The website prevents casting multiple votes for the same user and poll.
* Foreign key validity test
  * The user_id in the Votes Table references a valid user_id in the Users Table.
  * The poll_id in the Votes Table references a valid poll_id in the Polls Table.

### Actual result:

* Vote recording test
   * The vote is entered into the Votes Table successfully.
   * The SQL query retrieves the correct vote from the Votes Table.
* Multiple votes test
   * The website prevents casting multiple votes for the same user and poll.
* Foreign key validity test
  * The user_id in the Votes Table references a valid user_id in the Users Table.
  * The poll_id in the Votes Table references a valid poll_id in the Polls Table.

### Status:

Pass

### Notes:

These tests confirm the following:
  * New votes are correctly entered into and retrieved from the Votes Table.
  * Users are unable to cast multiple votes for the same poll.
  * A valid user_id is referenced for each vote in the Votes Table.
  * A valid poll_id is referenced for each vote in the Votes Table.

### Post-conditions:

* The vote is contained within the Votes Table and is linked to the correct poll.
* The vote is added to the total number of votes collected for a specific poll.





