#! /usr/bin/env python3
# coding: utf-8


import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') \
        or "this-is-the-default-secret-key"
