from crypt import methods
from flask import Blueprint,render_template,request, flash

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
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        # some extremely primitive validations
        if len(email) < 4:
            flash('Email must be at least 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First Name must be at least 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password length must be at least 6 characters.', category='error')
        else:
            flash('Account Created', category='success')
            #add user to DB

    return render_template("sign_up.html")
    # return "<p>Sign-up<p>"