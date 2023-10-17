# Cat

### Web Page: Taking an Existing Poll (Individual Page)

#### User Story:
As a Pollaris user, I want to be able to access and take a poll that has already been created by another user. I expect the poll to have a unique URL that can be accessed by both guest users and logged-in users. When I view the poll page, I should be able to see all the multiple-choice questions, select my preferred answers, and submit my responses. The data from my responses should be stored appropriately for analysis. If I'm a logged-in user, I also want the poll to be saved to my profile dashboard to record the history of the polls I have taken.

#### Acceptance Criteria (Verification List):
* A unique URL is generated for each created poll, and it is accessible to both guest users and logged-in users. The unique URL should also function as the unique poll identifier in the database.
* When I access the poll via the URL, I am presented with a clear and user-friendly interface that displays all the questions in the poll, each with their respective answer choices.
* I can select one answer choice for each multiple-choice question by interacting with radio buttons, checkboxes, or other input elements defined in Ryan's User Story.
* After I have selected my answers for all questions in the poll, I am able to submit my responses by clicking a "Submit" button.
* The submitted responses are stored in the app's database, associating them with the unique poll identifier and the user ID (if they are logged in, otherwise store as "Guest").
* Verify that the "Submit" button functions correctly, ensuring that it records the responses in the database. 
* I am provided with feedback (if incorrect/incomplete) or confirmation (if successful) after submitting my responses.
* The poll system should ensure that a user can only submit their response once for a specific poll, to prevent multiple submissions by the same user.
* If I'm a logged-in user, the poll is saved to my profile dashboard, allowing me to review the history of the polls I have taken.

# Ryan

# Greg

# Brandon
