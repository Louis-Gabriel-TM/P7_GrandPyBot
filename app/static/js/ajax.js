function responseTreatment(data) {
    var data = JSON.parse(data);
    console.log("Le serveur Python a renvoyé :", data);
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

$('#submit').on('click', function() {
    var user_query = document.getElementById('user_query').value;
    if (user_query !== "") {
        userValidated(user_query);
    }
});

$(document).on('keydown', function(event) {
    var userQuery = document.getElementById('user_query').value;
    var key = event.keyCode;
    if (key === 13 && userQuery !== "") {
        userValidated(userQuery);
    }
});

function userValidated(userQuery) {
    console.log("vous avez saisi : " + userQuery);
    displayAltaira(userQuery);
    var userZone = document.getElementById("user_query");
    userZone.value = "";
    ajaxPost('/ajax', userQuery, responseTreatment);
}

function ajaxPost(url, data, callback) {
    displayLoader();
    var req = new XMLHttpRequest();
    req.open('POST', url);
    req.addEventListener('load', function() {
        // A MODIFIER EN PRODUCTION : supprimer req.status === 0
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


