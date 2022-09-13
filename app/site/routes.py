from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Entry
from flask_login import LoginManager
from additemform import AddItemForm

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')