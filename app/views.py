from flask import flash, render_template

from app import app
from app.forms import ChatForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ChatForm()
    if form.validate_on_submit():
        flash("Robby vous as entendu.")
    return render_template('index.html', form=form)
