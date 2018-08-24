/*
Robby the GrandPy Bot,
7th project of OC Python Developer Path.
Author: Loïc Mangin
*/


function displayLoader()
// Display gif loader (used during AJAX request)
{
    var chatWindow = document.getElementById('chatwindow')
    var loaderZone = document.createElement('div');
    loaderZone.setAttribute('id', 'ajax-loader');
    var loader = document.createElement('img');
    loader.setAttribute('src', '../static/img/ajax-loader.gif');
    loader.setAttribute('alt', "Ajax loader");
    loaderZone.appendChild(loader);
    chatWindow.appendChild(loaderZone);
}

function removeLoader()
// Remove gif loader when AJAX request finished
{
    var loaderZone = document.getElementById('ajax-loader');
    loaderZone.remove();
}

function displayAltaira(speech)
// Display a chat bubble in 'altaira' style
{
    var chatWindow = document.getElementById('chatwindow');
    var speechZone = document.createElement('div');
    speechZone.classList.add('altaira');
    speechZone.textContent = speech;
    chatWindow.appendChild(speechZone);
}

function displayRobby(speech)
// Display a chat bubble in 'robby' style
{
    var chatWindow = document.getElementById('chatwindow');
    var speechZone = document.createElement('div');
    speechZone.classList.add('robby');
    speechZone.textContent = speech;
    chatWindow.appendChild(speechZone);
}

function initMap(coord)
// Display the Google Map and marker corresponding to coordinates
{
    var chatWindow = document.getElementById('chatwindow');
    var mapZone = document.createElement('div');
    mapZone.classList.add('map');
    mapZone.style.display = 'block';
    chatWindow.appendChild(mapZone);
    var map = new google.maps.Map(mapZone, {
        zoom: 16,
        center: coord,
        /* Google Maps Retro Style */
        styles: [
            {"elementType": "geometry", "stylers": [{"color": "#ebe3cd"}]},
            {"elementType": "labels.text.fill", "stylers": [{"color": "#523735"}]},
            {"elementType": "labels.text.stroke","stylers": [{"color": "#f5f1e6"}]},
            {
              "featureType": "administrative",
              "elementType": "geometry.stroke",
              "stylers": [{"color": "#c9b2a6"}]
            },
            {
              "featureType": "administrative.land_parcel",
              "elementType": "geometry.stroke",
              "stylers": [{"color": "#dcd2be"}]
            },
            {
              "featureType": "administrative.land_parcel",
              "elementType": "labels.text.fill",
              "stylers": [{"color": "#ae9e90"}]
            },
            {
              "featureType": "landscape.natural",
              "elementType": "geometry",
              "stylers": [{"color": "#dfd2ae"}]
            },
            {
              "featureType": "poi",
              "elementType": "geometry",
              "stylers": [{"color": "#dfd2ae"}]
            },
            {
              "featureType": "poi",
              "elementType": "labels.text.fill",
              "stylers": [{"color": "#93817c"}]
            },
            {
              "featureType": "poi.park",
              "elementType": "geometry.fill",
              "stylers": [{"color": "#a5b076"}]
            },
            {
              "featureType": "poi.park",
              "elementType": "labels.text.fill",
              "stylers": [{"color": "#447530"}]
            },
            {
              "featureType": "road",
              "elementType": "geometry",
              "stylers": [{"color": "#f5f1e6"}]
            },
            {
              "featureType": "road.arterial",
              "elementType": "geometry",
              "stylers": [{"color": "#fdfcf8"}]
            },
            {
              "featureType": "road.highway",
              "elementType": "geometry",
              "stylers": [{"color": "#f8c967"}]
            },
            {
              "featureType": "road.highway",
              "elementType": "geometry.stroke",
              "stylers": [{"color": "#e9bc62"}]
            },
            {
              "featureType": "road.highway.controlled_access",
              "elementType": "geometry",
              "stylers": [{"color": "#e98d58"}]
            },
            {
              "featureType": "road.highway.controlled_access",
              "elementType": "geometry.stroke",
              "stylers": [{"color": "#db8555"}]
            },
            {
              "featureType": "road.local",
              "elementType": "labels.text.fill",
              "stylers": [{"color": "#806b63"}]
            },
            {
              "featureType": "transit.line",
              "elementType": "geometry",
              "stylers": [{"color": "#dfd2ae"}]
            },
            {
              "featureType": "transit.line",
              "elementType": "labels.text.fill",
              "stylers": [{"color": "#8f7d77"}]
            },
            {
              "featureType": "transit.line",
              "elementType": "labels.text.stroke",
              "stylers": [{"color": "#ebe3cd"}]
            },
            {
              "featureType": "transit.station",
              "elementType": "geometry",
              "stylers": [{"color": "#dfd2ae"}]
            },
            {
              "featureType": "water",
              "elementType": "geometry.fill",
              "stylers": [{"color": "#b9d3c2"}]
            },
            {
              "featureType": "water",
              "elementType": "labels.text.fill",
              "stylers": [{"color": "#92998d"}]
            }
          ]
        });
        var marker = new google.maps.Marker({
            position: coord,
            map: map
        });
      }
