from flask import Blueprint

#bunch of roots defined here
auth = Blueprint('auth', __name__)




@auth.route('/login')
def login():
    return "<p>Login<p>"

@auth.route('/logout')
def logout():
    return "<p>Logout<p>"

@auth.route('/sign-up')
def signup():
    return "<p>Sign-up<p>"