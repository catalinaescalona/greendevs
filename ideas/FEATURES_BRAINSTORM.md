#### This document is intended to gather each team member's ideas about the basic features of the project (mockups, webpage designs, database designs, etc.). 

# Ryan

Potential tools for project:
* Flask - for backend framework
* REST API - for front/back end communication
* ReactJS - for frontend framework
* HTML/CSS - for structure and style of website
* MySQL - for database management system
* Jest - for testing
* Git - for version control

Potential pages for project website:
* home page with login form
* poll list page with list of polls (search, categories, filtering)
* poll pages with individual poll details (question, answer choices, submit button)
* poll results pages with answer data (poll results, graph)


# Brandon

Potential tools for Pollaris:

Frontend:  
* HTML - Provide structure  
* CSS - Styling and Design  
* React (JS Library) - User interface, excellent for single-page applications

Backend:  
* Flask - I don't know much about Flask, but it looks like an excellent Python framework for building a polling site.  
* Express JS - This is an alternative to using Flask. Built on Node js, looks great for building web apps.

Database Management:  

  Two options below, depending on if we were to go with Flask or Express JS.
  
* Flask-SQLAlchemy - Flask extension that adds support for SQLAlchemy. Will allow us to manage SQL databases using Python.  
* Express JS/Mongo DB - If we go with Express JS, it allows us to work with MongoDB.

  I prefer Python/Flask/SQLAlchemy over ExpressJS/MongoDB.

Website Layout:  

* Homepage: Logo in top left-hand corner, navigation links such as create poll, create user, login etc.  
* Create Poll Page: This could also be the homepage for simplicity. Allows user to create a poll.  
* About/FAQ Page: Describe the purpose of the site, answer simple questions.  
* *Optional - Browse Recent Polls Page: Depending on how long all this takes, if we have time, maybe have a page that shows recent or popular polls.

# Greg

Features:
  * After creating a poll, share on social media (maybe too much?) and email to increase participation.
  * Password recovery
  * add demographic info questions to polls to get an aggregate view of who is completing polls
  * anonymous response option

Additional tools not mentioned above:
  * Seaborn for heatmap of poll results

# Cat

General brainstorming ideas, in no particular order:
* Database tables should include info about users, polls, questions, responses. We need to really consider the relationships between the tables well before implementing them
* Seaborn / D3.js for data visualization
* Personal interest: integrate some graphics from p5.js for a more creative coding element, to visualize the data from the polls in a more artistic way than just traditional graphs
* Maybe we can find a way to trigger emails/messages/notifications to be sent to the user and/or their friends/network when a poll has been made, a poll is closed and ready to visualize, someone comments on the poll, etc.
* Is there a way to ensure that a user only votes in a poll once?
* We need to consider the different question types (ex: multiple choice, text input) and how the user can make them customizable
* I think we need to pick the most important features that we would consider as a "bare minimum" to make a poll, and prioritize building those features first
