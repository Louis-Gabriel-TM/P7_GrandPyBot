$('#submit').on('click', function() {
    var req = new XMLHttpRequest();

    req.onreadystatechange = function() {
        if (req.readySate === XMLHttpRequest.DONE) {
            // A MODIFIER EN PRODUCTION : éliminer req.status === 0
            if (req.status === 200 || req.status === 0) {
                alert("Le serveur Python a renvoyé : ", req.reponseText);
            }
        }
    }

    req.open('POST', '/ajax')
    req.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

    var query = document.getElementById('user_query').value;
    alert("vous avez saisi : " + query);

    req.send(query)

    alert("Requête envoyée !")
})