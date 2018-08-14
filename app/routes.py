#! /usr/bin/env python3
# coding: utf-8


from flask import flash, jsonify, render_template, request

from app import app
from app.forms import ChatForm
from .tools.parser import Parser
from .tools.ask_gmaps import GMapsRequest
from .tools.ask_wiki import WikiRequest
from .tools.credentials import GMAPS_KEY


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ChatForm()
    return render_template('index.html', form=form, key=GMAPS_KEY)

@app.route('/ajax', methods=['POST'])
def ajax_request():

    user_query = request.data.decode('utf-8')
    print("Contenu de la requête =", user_query)
    
    parser = Parser()
    cleaned_query = parser.clean(user_query)
    print("Requête nettoyée =", cleaned_query)
    
    gmaps_request = GMapsRequest(cleaned_query)
    coord = gmaps_request.get_coord()
    print("Coordonnées GMaps =", coord)
    
    if coord:      
        wiki_request = WikiRequest(coord['lat'], coord['lng'])
        #page_id = wiki_request.page_id
        extract = wiki_request.extract
        response = {'coord': {'lat': coord['lat'],'lng': coord['lng']},
                    'extract': extract
                   }
        print(" >>>", extract)
    else:
        response = {'coord': {'lat': None,'lng': None},
                    'extract': None
                   }
    
    print("RESPONSE >>>", response)
    print("JSONIFIED RESPONSE >>>", response)

    return jsonify(response)
