// JavaScript page for Pollaris Create Page
// Authors: Escalona, Sansbury, Webster
// Written December 2023
// CSPB 3308 - Fall 2023 - Knox - Software Development Tools and Methods
// University of Colorado Boulder


// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Add an event listener to the "Create Poll" button
    const createPollButton = document.getElementById("create-poll-button");
    createPollButton.addEventListener("click", createPoll);

    // Function to create a new poll and send data to the Flask backend
    function createPoll() {
        // Get the question and options from the form
        const question = document.getElementById("question").value;
        const options = Array.from(document.querySelectorAll(".option-input")).map((input) => input.value);

        // Create an object to hold the poll data
        const pollData = {
            question: question,
            options: options,
        };

        // Send the pollData object as JSON to the Flask backend
        fetch("/create", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(pollData),
        })
            .then((response) => response.json())
            .then((data) => {
                // Handle the response from the server (e.g., show a success message or redirect)
                console.log("Poll created successfully:", data);
                // You can add your own logic here for handling the response
            })
            .catch((error) => {
                console.error("Error creating poll:", error);
                // Handle errors (e.g., display an error message)
            });
    }
});
