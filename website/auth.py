from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# define authorisation routes

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in succesfully!', category="success")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Password incorrect, try again.", category='error')
        else:
            flash('Username does not exist.', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
# login_required means cannot access logout function without being logged in
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    
@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(username=username).first()
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists. Please choose a different username.", category='error')
        else:
            if len(username) < 3:
                flash("Username must be greater than 4 characters.", category='error')
            elif len(first_name) < 2:
                flash("First name must be greater than 1 character.", category='error')
            elif password1 != password2:
                flash("Passwords do not match.", category='error')
            elif len(password1) < 7:
                flash("Password must be greater than 6 characters.", category='error')
            else:
                # create a new user and give it a password hash based on the method below
                new_user = User(username=username, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
                # add user to database session
                db.session.add(new_user)
                # commit database session
                db.session.commit()
                # perform flask_login login_user function
                login_user(new_user, remember=True)
                flash("Account created!", category='success')
                return redirect(url_for('views.home'))
            
    return render_template("sign_up.html", user=current_user)