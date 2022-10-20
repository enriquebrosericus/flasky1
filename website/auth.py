from crypt import methods
from flask import Blueprint,render_template,request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

#bunch of roots defined here
auth = Blueprint('auth', __name__)




@auth.route('/login',methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", text="Test", boolean=False)
    # return "<p>Login<p>"

@auth.route('/logout')
def logout():
    return "<p>Logout<p>"

@auth.route('/sign-up',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        # some extremely primitive validations
        if len(email) < 4:
            flash('Email must be at least 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First Name must be at least 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password length must be at least 6 characters.', category='error')
        else:
            # flash('Account Created', category='success')
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method = 'sha256'))
            #add user to DB
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

            #redir to homepage


    return render_template("sign_up.html")
    # return "<p>Sign-up<p>"