#! /usr/bin/env python3
# coding: utf-8


"""
Robby the GrandPy Bot,
7th project of OC Python Developer Path.
Author: Loïc Mangin
"""


import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') \
        or "this-is-the-default-secret-key"
