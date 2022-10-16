from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route("/coffeegonewild")
def index():
    return render_template("splash.html")

@app.route("/coffeegonewild/home")
def home():
    return render_template("index.html")

# REGISTER/CREATE A USER
# to show the registration form
@app.route("/coffeegonewild/register")
def registration_form():
    return render_template("register.html")

# action route to register a user
@app.route("/coffeegonewild/add_user", methods=["POST"])
def create():
    if not User.validate(request.form):
        return redirect('/coffeegonewild/register')
    hashed_pw = bcrypt.generate_password_hash(request.form['password']) 
    data = {
        **request.form,
        'password': hashed_pw
    }
    session['user_id'] = User.create(data)
    session['user_name'] = request.form['user_name']
    return redirect("/coffeegonewild" )

# LOGIN
# to show the login form
@app.route("/coffeegonewild/login_form")
def login_form():
    return render_template("login.html")

@app.route("/coffeegonewild/login", methods=['POST'])
def login():
    data = {
        'user_name': request.form['user_name']
    }
    user_from_db = User.get_by_user_name(data)
    if not user_from_db:
        flash("Invalid Credentials", "log")
        return redirect('/coffeegonewild/login_form')
    if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
        flash("Invalid Credentials", "log")
        return redirect('/coffeegonewild/login_form')
    session['user_id'] = user_from_db.id
    session['user_name'] = user_from_db.user_name 
    return redirect("/coffeegonewild/home")

# LOGOUT
@app.route("/coffeegonewild/logout")
def logout():
    session.clear()
    return redirect('/coffeegonewild/home')