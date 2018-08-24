#! /usr/bin/env python3
# coding: utf-8


"""
Robby the GrandPy Bot,
7th project of OC Python Developer Path.
Author: Loïc Mangin
"""


from flask import Flask

from config import Config


app = Flask(__name__)
app.config.from_object(Config)


from app import routes
