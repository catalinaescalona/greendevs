# Pollaris - Project Tables and Functions



### Table Name: 

Polls Table

### Description:

This table stores individual poll information.

### Table Fields:

* poll_id - primary key
* user_id - foreign key to users table
* question - text questions
* options - JSON column to store options as arrays
* create_date - poll creation timestamp
* expiration_date - poll expiration date

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

