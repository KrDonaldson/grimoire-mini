from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models import db, User, Entry, entry_schema, entries_schema
from flask_login import current_user
from additemform import AddItemForm

api = Blueprint('api',__name__, url_prefix='/journal')

@api.route('/', methods = ['GET'])
def get_entries():
    a_user = current_user.id
    entry = Entry.query.filter_by(user_id = a_user).all()
    response = entries_schema.dump(entry)
    return render_template('journal.html', entries = response)

@api.route('/entry', methods=['POST', 'GET'])
def create_entry():
    form = AddItemForm()
    try:
        if request.method == 'POST':
            name = form.name.data
            details = form.details.data
            user_id = current_user.id

            entry = Entry(name=name, details=details, user_id=user_id)
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('api.get_entries'))
    except:
        print('did not go through for whatever reason')
    return render_template('addEntry.html', form=form)

@api.route('/remove/<id>', methods = ['DELETE'])
def delete_entry(id):
    entry = Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    
