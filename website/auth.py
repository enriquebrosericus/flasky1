from crypt import methods
from xmlrpc.client import boolean
from flask import Blueprint,render_template,request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

#bunch of roots defined here
auth = Blueprint('auth', __name__)




@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email') 
        password = request.form.get('password')

        # check to see if we have a user with that email address
        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password!', category='error')
        else:
            flash('email does not exist!', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #determine if email is already registered
        user=User.query.filter_by(email=email).first()
        print("i am user from the db: ", user)

        if user:
            flash('Email is already registered!', category='error')
        # some extremely primitive validations
        elif len(email) < 4:
            flash('Email must be at least 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First Name must be at least 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 6:
            flash('Password length must be at least 6 characters.', category='error')
        else:
            # flash('Account Created', category='success')
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method = 'sha256'))
            #add user to DB
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))

            #redir to homepage


    return render_template("sign_up.html", user=current_user)
    # return "<p>Sign-up<p>"