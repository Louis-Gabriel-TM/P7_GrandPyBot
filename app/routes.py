#! /usr/bin/env python3
# coding: utf-8


from flask import flash, render_template

from app import app
from app.forms import ChatForm
from .tools.parser import Parser
from .tools.ask_gmaps import GMapsRequest
from .tools.ask_wiki import WikiRequest


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ChatForm()
    ps = Parser()

    if form.validate_on_submit():
        to_api = ps.clean(form.user_request.data)
        flash("Robby vous as entendu et retient : {}".format(to_api))

        gm = GMapsRequest(to_api)
        coord = gm.get_coord()
        flash("Robby a obtenu les coordonnées {}".format(coord))

        wk = WikiRequest(to_api)
        extract = wk.get_extract()
        flash("Robby a récupéré les infos suivantes : {}".format(extract))

    return render_template('index.html', form=form)
