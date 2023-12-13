// JavaScript page for Pollaris Homepage
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
                window.location.href = response.login_url;
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

    // clicking create a poll button redirects to create page
    $("#create-btn").on("click", function() {
        $.ajax({
            type: 'GET',
            url: '/redirect_create',
            success: function(response) {
                // redirect to create URL
                window.location.href = response.create_url;
            }
        });
    });

    // clicking any of the poll links redirects to vote page
    $(".poll-links").on("click", function() {
        $.ajax({
            type: 'GET',
            url: 'redirect_vote',
            success: function(response) {
                // redirect to vote URL
                window.location.href = response.vote_url;
            }
        });
    });
});