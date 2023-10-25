# Pollaris Web Pages Design (Project Milestone 4)

Wireframe slides: https://docs.google.com/presentation/d/1sW2sKaVMMQkeEu7C5ovWATHitEbHIE86Xp1X2B5vn9s/edit?usp=sharing
---
# Page 1 - Home
### Page Title
### Page Description and Mockup
### Parameters needed for the page
### Data needed to render the page
### Link destinations for the page
### List of tests for verifying the rendering of the page

---
# Page 2 - Login
### Page Title
### Page Description and Mockup
### Parameters needed for the page
### Data needed to render the page
### Link destinations for the page
### List of tests for verifying the rendering of the page

---
# Page 3 - Create a Poll
### Page Title
### Page Description and Mockup
### Parameters needed for the page
### Data needed to render the page
### Link destinations for the page
### List of tests for verifying the rendering of the page

---
# Page 4 - Take a Poll
### Page Title: Take a Poll
### Page Description and Mockup
This page displays a poll already created by another user. The title of the poll is displayed at the top, followed by a poll description and information about who created the poll and when. The poll questions are listed in the page and the user can select one answer. If the poll taker is logged in, they should be able to hit the save button to save their responses. After answering all of the questions on the page, the poll taker can hit the submit button. This will take them to the poll results page. If the user is logged in, the poll should be saved to the user profile dashboard to record the history of polls they have taken. If they are not logged in, the poll results should be saved under "Guest" user.

### Parameters needed for the page
* unique poll ID
* user authentication status (check if user is logged in or not)
  
### Data needed to render the page
* poll title
* poll description
* poll creator's information (username, timestamp of creation)
* poll question and answer options
* user/guest recorded answers to the poll questions
* user/guest ID for saving the poll (to save to user dashboard, or recored in DB as guest)
  
### Link destinations for the page
* poll creator name link: takes user to the poll creator's profile 
* save button: allows users to save their responses to the poll
* submit button: takes user to poll results page
* if user is logged in, profile button at the top: takes them to their profile dashboard (which should list the polls they have taken, including this one after they hit submit)
* if user is not logged in, login button: takes them to the login page
  
### List of tests for verifying the rendering of the page
* basic rendering test - ensure page displays the correct information
* user authentication test - check status if user is logged in or not
* user interaction tests:
    * make sure user can select answers to the poll questions
    * make sure save button saves the responses
    * make sure submit button takes user to the poll results page
* data retrieval tests:
    * check that poll data was retrieved correctly from database using unique poll id
    * check that poll responses recorded correctly in DB
    * if user is logged in, check that poll is added to their user profile dashboard
* error handling tests - ensure that all poll questions on page have been answered
* consistency tests - make sure the style is consistent with the other web pages
* responsiveness test - make sure this page works on different devices and screen sizes


---
# Page 5 - Popular Polls
### Page Title: Popular Polls
### Page Description and Mockup
The Popular Polls page will list polls already created by other users. The user will be able to choose to sort the polls by popular, trending, and new. The user will then be able to vote on the polls, see the results, and share them. 

![Screenshot 2023-10-24 155822](https://github.com/catalinaescalona/greendevs/assets/143830239/e7db0e96-4743-4c53-ab4a-5210dc0f56c2)

### Parameters needed for the page
* User Registration
* User Login
* Poll Browsing
* Poll Filtering
* Answer Options (Multiple Choice Only)
* Algorithms for Trending, Popular, and New Polls
* Moderation and Reporting
* Community Guidelines
* Sharing Options
* Privacy and Security
* Data needed to render the page
* Link destinations for the page
### Data needed to render page
* User Data
* Poll Data
* Engagement Metrics (Number of votes etc.)
* User Interaction (Polls users has voted on, polls they have created etc.)
* Moderation Data
* Page Layout and Styling
* Analytics Data
* User Authentication
### Link destinations for the page
* Home Page
* Login
* User Profile
* Create A Poll
* Search
* Take A Poll (Vote)
* Report Content
* Share Poll
* Contact Us
* Privacy Policy
* Terms of Service
### List of tests for verifying the rendering of the page
* Create account testing
* Login testing
* Poll creation testing
* Voting testing
* Moderation testing
* Share Poll testing
* User Engagement Test
* Test different browers


