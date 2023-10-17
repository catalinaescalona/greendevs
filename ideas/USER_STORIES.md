# Cat

### Web Page: Taking an Existing Poll (Individual Page)

#### User Story:
As a Pollaris user, I want to be able to access and take a poll that has already been created by another user. I should be able to see the title of the poll at the top of the page, followed by the creator's name and a link to their user profile. I expect the poll to have a unique URL that can be accessed by both guest users and logged-in users. When I view the poll page, I should be able to see all the multiple-choice questions, select my preferred answers, and submit my responses. The data from my responses should be stored appropriately for analysis. When I hit the "Submit" button, it should take me to the visualized results of the poll. Finally, if I'm a logged-in user, I also want the poll to be saved to my profile dashboard to record the history of the polls I have taken. 

#### Mockup / Visualization:
![2023-10-17](https://github.com/catalinaescalona/greendevs/assets/68168149/83d034a4-7f09-4809-972a-856b556262da)


#### Acceptance Criteria (Verification List):
* A unique URL is generated for each created poll, and it is accessible to both guest users and logged-in users. The unique URL should also function as the unique poll identifier in the database.
* When I access the poll via the URL, I am presented with a clear and user-friendly interface that displays the title of the poll at the top, followed by the creator's name, which links to their user profile. Clicking on the creator's name should take me to their profile page, which lists all the polls they have created and taken. 
* Below the poll title and creator information, I should see all the multiple-choice questions, each with their respective answer choices.
* I can select one answer choice for each multiple-choice question by interacting with radio buttons, checkboxes, or other input elements defined in Ryan's User Story.
* After I have selected my answers for all questions in the poll, I am able to submit my responses by clicking a "Submit" button.
* I am provided with feedback (if incorrect/incomplete) or confirmation (if successful) after submitting my responses.
* The "Submit" button takes me to the visualized results of the poll, where I can view the poll's statistics and see how others have responded.
* The submitted responses are stored in the app's database, associating them with the unique poll identifier and the user ID (if they are logged in, otherwise store as "Guest").
* Verify that the "Submit" button functions correctly, ensuring that it records the responses in the database.
* The poll system should ensure that a user can only submit their response once for a specific poll, to prevent multiple submissions by the same user.
* If I'm a logged-in user, the poll is saved to my profile dashboard, allowing me to review the history of the polls I have taken.

#### Pages we will need for this to work:
* Create a poll page, to create the poll in the first place
* Visualization page of poll results
* User profile page for poll creator
* User profile page for logged-in poll taker


# Ryan

### Page: Create a Poll

#### User Story:
As a Pollaris user, I want to be able to create a new poll on the site. The create a poll page should be simple, intuitive, and easy to use. There should be individual sections that accept text input where I can create a poll title, add a poll description, and create the poll answer options. There should be a ‘create poll’ button at the bottom of the page that submits the data and creates the poll on the site with a unique URL.

#### Acceptance Criteria:
* Access - once logged in, there should be a create a poll link in the website menu
* Creation - there should be a form that has fields for creating the question, description, and answer options. (can add or remove number of answer fields)
* Preview - there should be a button at the bottom of the page to allow for previewing the poll before submitting to the site. The preview page should allow for the user to go back and edit the poll if necessary.
* Validation - the page should validate that each setion is filled out correctly and give an error if not (500 characters max per field, text only, cannot be blank)
* Confirmation - there should be a confirmation message stating the poll has been created after the user clicks the submit button.
* Sharing - there should be a unique URL and ‘click to copy’ button in the confirmation message.

#### Mockups:

![Screenshot 2023-10-17 at 9 24 14 AM](https://github.com/catalinaescalona/greendevs/assets/143199876/8a843699-1e02-41d6-9797-a7fd8b4fd058)

![Screenshot 2023-10-17 at 9 24 41 AM](https://github.com/catalinaescalona/greendevs/assets/143199876/73a311b1-b0be-48ce-8bea-823c431ce034)

![Screenshot 2023-10-17 at 9 24 54 AM](https://github.com/catalinaescalona/greendevs/assets/143199876/ee32ced6-8fb2-46d2-8c6a-b3e22631c3f1)


# Greg

#User Story 1:
* As a user
* I want to be able to enter my username and password to be able to securely access my account
* So I can access my account information and polls
  

#User Story 2:
* As a user
* I want to be able to create an account
* So I can change settings and have all of my polls saved in one place
  

#User Story 3:
* As a system administrator
* I want there to be an automated way for users to change their password if they forget it
* So that they can change password efficiently with no manual processes that gets in the way
  

#User Story 4:
* As a system administrator
* I want to ensure that an account exists and can only be accessed with the correct credentials
* So that we can be sure users are only able to access their data

# Brandon

### User Story for "Take a Poll" Page

As a Pollaris user,
I want to view and participate in polls created by other users,
So that I can contribute my opinion and see the results of other polls.

#### Acceptance Criteria:

* When I navigate to the "Take a Poll" page on Pollaris, I should see a list of available polls to take created by others.
* I should be able to rank the polls by Popularity, Trending, or New.
* Each poll should display its title/question and a brief description or snippet.
* When I see a poll I want to take, I will click a "Take Poll" button that will take me to that polls page.
* On the poll's detail page, I should see the poll question and all its options.
* I can select an option and click on a "Vote" button to cast my vote if I am logged in. If not, I will be prompted to login.
* After voting, I should immediately see the current results of the poll, and then a button below that saying "Take another poll!" which takes me back to the "Take a Poll" page.

#### Mockup:

![mockup](https://github.com/catalinaescalona/greendevs/assets/143830239/ed13b508-5317-4d09-bb60-30f5a2ff682e)





