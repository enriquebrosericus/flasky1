from crypt import methods
from unicodedata import category
from xmlrpc.client import boolean
from flask import Blueprint, flash, jsonify,render_template, request
from flask_login import login_required,  current_user
from .models import Note
from . import db
import json

#bunch of routes defined here
views = Blueprint('views', __name__)


#homepage root
#decorator
@views.route('/', methods=['GET','POST'])
@login_required
def home():
    # return "<h1>Test<h1>"
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) <1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(note=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note Created!', category='success')

    return render_template("home.html", user=current_user )



@views.route('/delete-note', methods=['POST'])
def delete_note():
    note=json.loads(request.data)
    noteId = note['noteId']
    note=Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note Deleted!', category='success')
            
        return jsonify({})



# @views.route('/login')
# def login():
#     # passing variable text to the login.html, where the variable is interpolated between curly braces
#     return render_template("login.html", text="Test", boolean=False)


# @views.route('/sign-up')
# def signup():
#     return render_template("sign_up.html")

# @views.route('/logout')
# def logout():
#     # return "<h1>Logout<h1>"
#     return render_template("home.html")