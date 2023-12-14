// JavaScript page for Pollaris Sign Up Page
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
        $.ajax({
            type: 'GET',
            url: '/redirect_login',
            success: function(response) {
                // redirect to login URL
                window.location.href = '/login';
            }
        });
    });

    // clicking sign up button redirects to sign up page
    $("#signup-btn").on("click", function() {
        // get the form data
        var formData = {
            username: $("input[name='username']").val(),
            first: $("input[name='first']").val(),
            last: $("input[name='last']").val(),
            email: $("input[name='email']").val(),
            password: $("input[name='password']").val()
        };
        // send data to backend using AJAX
        $.ajax({
            type: 'POST',
            url: '/signup',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify(formData),
            success: function(response) {
                // handle response from the server
                console.log(response);
                // redirect or show a success message based on the response
                window.location.href = response.redirect_url;
            },
            error: function(error) {
                // handle the error
                console.error(error);
                // display error message to the user
                alert('Error with Sign Up. Please try again!');
            }
        });
    });
});
