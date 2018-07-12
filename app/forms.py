#! /usr/bin/env python3
# coding: utf-8


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ChatForm(FlaskForm):
    user_request = StringField(
        "Dis-moi Robby, ...", validators=[DataRequired()]
        )
    submit = SubmitField("Dire")
