from xmlrpc.client import boolean
from flask import Blueprint,render_template

#bunch of routes defined here
views = Blueprint('views', __name__)


#homepage root
#decorator
@views.route('/')
def home():
    # return "<h1>Test<h1>"
    return render_template("home.html")


@views.route('/login')
def login():
    # passing variable text to the login.html, where the variable is interpolated between curly braces
    return render_template("login.html", text="Test", boolean=False)


@views.route('/sign-up')
def signup():
    return render_template("sign_up.html")

@views.route('/logout')
def logout():
    return "<h1>Logout<h1>"
    # return render_template("home.html")