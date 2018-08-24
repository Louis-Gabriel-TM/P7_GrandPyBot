/*
Robby the GrandPy Bot,
7th project of OC Python Developer Path.
Author: Loïc Mangin
*/


$('#submit').on('click', function()
// Handles user submission with 'DIRE' button
{
    var user_query = document.getElementById('usset er_query').value;
    if (user_query !== "") {
        userValidated(user_query);
    }
});

$(document).on('keydown', function(event)
// Handles user submission with 'RETURN' key
{
    var userQuery = document.getElementById('user_query').value;
    var key = event.keyCode;
    if (key === 13 && userQuery !== "") {
        userValidated(userQuery);
    }
});

function userValidated(userQuery)
// Display user query in chat window, clear form and init ajax request
{
    console.log("vous avez saisi : " + userQuery); // FOR DEBUG
    displayAltaira(userQuery);
    var userZone = document.getElementById("user_query");
    userZone.value = "";
    ajaxPost('/ajax', userQuery, responseTreatment);
}

function ajaxPost(url, data, callback)
// Display gif loader, prepare and send ajax 'POST' request
{
    displayLoader();
    var req = new XMLHttpRequest();
    req.open('POST', url);
    req.addEventListener('load', function() {
        if ((req.status >= 200 && req.status < 400)) {
            callback(req.responseText);
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });
    req.addEventListener('error', function() {
        console.error("Erreur réseau avec l'URL " + url);
    });
    req.send(data);
}

function responseTreatment(data) 
// Get AJAX response, remove gif loader and display Robby answer
{
    var data = JSON.parse(data);
    console.log("Le serveur Python a renvoyé :", data); // FOR DEBUG
    removeLoader();
    if (data !== "") {
        displayRobby("Voici ce que j'ai trouvé Altaira :")
        initMap(data['coord']);
        if (data['extract'] !== "") {
            displayRobby(data['extract']);
        }
    } else {
        displayRobby("Désolé Altaira, je n'ai rien trouvé.")
    }
}
