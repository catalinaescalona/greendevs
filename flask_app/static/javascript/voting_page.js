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