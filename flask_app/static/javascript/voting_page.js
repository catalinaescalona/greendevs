// JavaScript page for Pollaris Voting Page
// Authors: Escalona, Sansbury, Webster
// Written December 2023
// CSPB 3308 - Fall 2023 - Knox - Software Development Tools and Methods
// University of Colorado Boulder

dict={}

function submitData() {
    var questions = document.getElementsByClassName("question");
    for (var j = 0, length = questions.length; j < questions.length; j++){
        let name ="q".concat((j+1).toString());
        var options = document.getElementsByName(name);
        let filled_out=false;
        for (var i = 0, length = options.length; i < length; i++) {
            if (options[i].checked) {
                filled_out = true
                dict[j]=options[i].value;
            }
        }
        if (filled_out==false){
            dict[j]="";
        }
    }
console.log(dict)
}

// Perform AJAX call to redirect to the homepage
    $.ajax({
        type: 'POST', 
        url: '/redirect_home',
        success: function (response) {
            // Redirect to home URL
            window.location.href = response.home_url;
        }
    });
}

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
});
