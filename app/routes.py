#! /usr/bin/env python3
# coding: utf-8


"""
Robby the GrandPy Bot,
7th project of OC Python Developer Path.
Author: Loïc Mangin
"""


from flask import jsonify, render_template, request

from app import app
from app.forms import ChatForm
from .tools.parser import Parser
from .tools.ask_gmaps import GMapsRequest
from .tools.ask_wiki import WikiRequest
from .tools.credentials import GMAPS_KEY


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    """Initiates the /index page (no other page in this app)
    """
    form = ChatForm()
    return render_template('index.html', form=form, key=GMAPS_KEY)


@app.route('/ajax', methods=['POST'])
def ajax_request():
    """Receives user request for parsing
    Then asks Google Maps for coordinates
    Then asks Media Wiki for a Wikipedia extract
    Returns coordinates and extract as a JSON object
    """
    user_query = request.data.decode('utf-8')
    print("Contenu de la requête =", user_query)  # FOR DEBUG

    parser = Parser()
    cleaned_query = parser.clean(user_query)
    print("Requête nettoyée =", cleaned_query)  # FOR DEBUG

    gmaps_request = GMapsRequest(cleaned_query)
    coord = gmaps_request.get_coord()
    print("Coordonnées GMaps =", coord)  # FOR DEBUG
    
    if coord:      
        wiki_request = WikiRequest(coord['lat'], coord['lng'])
        extract = wiki_request.get_extract()
        if extract:
            response = {'coord': {'lat': coord['lat'], 'lng': coord['lng']},
                        'extract': extract
                        }
        else:
            response = {'coord': {'lat': coord['lat'], 'lng': coord['lng']},
                        'extract': ""
                        }
        print(" >>>", extract)  # FOR DEBUG
    else:
        response = ""
    print("RESPONSE >>>", response)  # FOR DEBUG

    return jsonify(response)
