from flask import Blueprint, render_template, request, redirect, url_for, flash
from additemforms import AddItemForm
from models import db, Entry
from helpers import token_required
from flask_login import LoginManager

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/journal')
def journal():
    return render_template('journal.html')

@site.route('/addEntry', methods = ['GET', 'POST'])
# @token_required
def addEntry(current_user):
    form = AddItemForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            name = form.name.data
            details = form.details.data
            user_id = current_user.id

            entry = Entry(name=name, details=details, user_id=user_id)

            db.session.add(entry)
            db.session.commit()

            flash('Entry successfully added.')

            return redirect(url_for('site.journal'))
    except:
        raise Exception('Try again.')

    return render_template('addEntry.html', form=form)