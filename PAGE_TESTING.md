# Pollaris Web Pages Design (Project Milestone 4)

Wireframe slides: https://docs.google.com/presentation/d/1sW2sKaVMMQkeEu7C5ovWATHitEbHIE86Xp1X2B5vn9s/edit?usp=sharing
---
# Page 1 - Home
### Page Title: Pollaris Home Page

### Page Description and Mockup

<img width="567" alt="Pollaris_Home_Final" src="https://github.com/catalinaescalona/greendevs/assets/120431515/1132d345-4109-46ec-8569-525df52a21e8">

The Homepage is a central page that allows user to navigate to anywhere on the website. Users can get to the log in page and the sign up page to create an account. They can access the take a poll page to take public polls, as well as select from various featured public polls displayed at the bottom of the website. If they recieved a Poll ID they can enter it directly on the home page to go to the poll they are wanting to access. There is also a menu button that allows users to access additional information that we still need to decide on (about, privacy policy, contact, etc.)

### Parameters needed for the page

* Featured random/popular poll IDs to be displayed

### Data needed to render the page

* Featured random/popular poll unique IDs that are displayed on the bottom of the page

### Link destinations for the page

* Homepage
* Login page
* Take a poll page
* Sign up page to create account
* Menu with menu options still tbd (contact, terms of service, about, privacy policy, etc.)
* Text box to enter a shared poll id to take specific poll
* Button to go to entered poll id
* Various links to featured polls
* Bubble icons to move through featured polls at bottom of page
* Take a Poll page


### List of tests for verifying the rendering of the page

* Test that expected polls populate the bottom of the page
* Test that clicking featured polls redirects to correct poll page
* Test that entered poll id exists when searching for a poll
* Test that entered poll id throws error if invalid
* Test that valid poll id sends user to correct poll page
* Test that sign in and sign up buttons redirect to correct pages
* Test that the Pollaris logo redirects to/reloads home page
* Test that menu drops down and proper links are included
* Test menu links redirect to correct pages
* Test that 5(?) navigation bubbles shift the featured polls correctly
* Test that take a poll button redirects to the take a poll page

---
# Page 2 - Login
### Page Title: Pollaris Sign In/Login Page

### Page Description and Mockup

<img width="688" alt="Polaris_Login" src="https://github.com/catalinaescalona/greendevs/assets/120431515/63c60c22-c941-447c-9106-82f56875bc38">

The Login/Sign In page allows users to access their account. The main functionality includes two text boxes for username and password, and a button to sign in and be redirected to the user's individual dashboard. The header is fixed to the page, so they can access the home page by clicking the logo, reload the sign in page, and access the menu. There is also a link to the Sign Up page to create an account. Also password a recovery option.

### Parameters needed for the page

* Username
* Password

### Data needed to render the page

* No specific data needed to render the page

### Link destinations for the page

* Home Page
* Sign In Page (reload)
* Menu
* Sign Up page to create an account
* Log in Button to redirect to user dashboard
* Forgot Password link for password recovery
* Username text input box
* Password text input box
  
### List of tests for verifying the rendering of the page

* Test for valid username
* Test for valid password
* Test invalid username throws error
* Test invalid password throws error
* Test that user is redirected to correct user dashboard when entering valid credentials
* Test that the logo button in header sends user to home page
* Test that Sign In button in header reloads page/sends user to Sign In
* Test that Sign Up button sends user to Sign Up page to create an account
* Test that Forgot Password prompts user for email to complete that process
* Test that menu drops down
* Test that correct links are in the menu and redirect to correct pages

---
# Page 3 - Create a Poll
### Page Title: Create a Poll
### Page Description and Mockup
The create a poll page enables a user to make a new poll. The user will input a poll title, poll description, and poll answers within the body of the page. The user will be able to preview the poll before publishing by clicking the preview button and will then be able to publish the poll by clicking the submit button. 

![Screenshot 2023-10-25 at 1 40 08 PM](https://github.com/catalinaescalona/greendevs/assets/143199876/47dd53dd-e0ea-48a6-a8d4-465023090d61)

### Parameters needed for the page
* User authentication (must be logged in to create poll)
* Poll questions, description, and answer options (multiple choice only)
* Sharing options

### Data needed to render the page
* User authentication
* Unique poll ID
* User generated poll title
* User generated poll description
* User generated poll answers
* Poll creation timestamp

### Link destinations for the page
* Homepage
* Login
* User profile
* Poll preview page
* Poll submitted page (with sharing)
* Contact Us
* Privacy Policy
* Terms of Service
  
### List of tests for verifying the rendering of the page
* Test registration (user can make new account)
* Test login (user can login)
* Test poll creation
* Test question and answer length
* Test sharing
* Test different browsers
* Test database connectivity


---
# Page 4 - Take a Poll
### Page Title: Take a Poll
### Page Description and Mockup
This page displays a poll already created by another user. The title of the poll is displayed at the top, followed by a poll description and information about who created the poll and when. The poll questions are listed in the page and the user can select one answer. If the poll taker is logged in, they should be able to hit the save button to save their responses. After answering all of the questions on the page, the poll taker can hit the submit button. This will take them to the poll results page. If the user is logged in, the poll should be saved to the user profile dashboard to record the history of polls they have taken. If they are not logged in, the poll results should be saved under "Guest" user.

<img width="902" alt="Screen Shot 2023-10-26 at 19 59 36" src="https://github.com/catalinaescalona/greendevs/assets/68168149/c2739ed3-11a1-46ef-a76c-838762bb997d">

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


