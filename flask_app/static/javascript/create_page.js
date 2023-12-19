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

    function createPoll() {
    // Get the question and options from the form
    const question = document.getElementById("question").value;
    const options = Array.from(document.querySelectorAll(".option-input")).map((input) => input.value);

    // Create an object to hold the poll data, including poll_id
    const pollData = {
        question: question,
        options: options,
        poll_id: poll_id // Include the poll_id here
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
                // Handle the response from the server
                console.log("Response from the server:", data);
                if (data.success) {
                    // Poll created successfully, redirect to the success page
                    window.location.href = '/create_poll_success';
                } else {
                    // Handle any other response or errors here
                    console.error("Error creating poll:", data.message);
                    
                }
            })
            .catch((error) => {
                console.error("Error creating poll:", error);
                // Handle errors (e.g., display an error message)
            });
    }
});
