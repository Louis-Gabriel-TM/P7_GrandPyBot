function responseTreatment(data) {

    var data = JSON.parse(data);

    console.log("Le serveur Python a renvoyé :", data);

    initMap(data['coord']);

    var extract = document.getElementById('extract');
    extract.textContent = data['extract'];
}

function ajaxPost(url, data, callback) {

    var req = new XMLHttpRequest();
    req.open('POST', url);
      
    req.addEventListener('load', function() {
        // A MODIFIER EN PRODUCTION : supprimer req.status === 0
        if ((req.status >= 200 && req.status < 400) || req.status === 0) {
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

$('#submit').on('click', function() {

    // Capture saisie utilisateur
    var user_query = document.getElementById('user_query').value;

    console.log("vous avez saisi : " + user_query);

    ajaxPost('/ajax', user_query, responseTreatment);
})
