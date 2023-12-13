// JavaScript page for Pollaris Login Page
// Authors: Escalona, Sansbury, Webster
// Written December 2023
// CSPB 3308 - Fall 2023 - Knox - Software Development Tools and Methods
// University of Colorado Boulder

$(document).ready(function() {
    // clicking logo redirects to homepage
    $("#logo").on("click", function() {
        $.ajax({
            type: 'GET',
            url: '/redirect_home',
            success: function(response) {
                // redirect to home URL
                window.location.href = response.home_url;
            }
        });
    });
    
    // clicking login button redirects to login page
    $("#login-btn").on("click", function() {
        // get the form data
        var formData = {
            username: $("input[name='username']").val(),
            password: $("input[name='password']").val()
        };
        // send form data to backend using AJAX
        $.ajax({
            type: 'POST',
            url: '/login',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify(formData),
            success: function(response) {
                // handle response from server
                console.log(response);
                // redirect or show success message based on the response
                window.location.href = response.redirect_url;
            },
            error: function(error) {
                // handle error
                console.error(error);
                // display error message to the user
                alert('Error with Log In. Please try again!');
            }
        });
    });

    // clicking sign up button redirects to sign up page
    $("#sign-up-btn").on("click", function() {
        $.ajax({
            type: 'GET',
            url: '/redirect_signup',
            success: function(response) {
                // redirect to signup URL
                window.location.href = response.signup_url;
            }
        });
    });
});