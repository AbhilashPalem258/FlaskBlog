from flask import render_template, url_for, redirect, flash, request
from flaskblog.models import User, Post
from flaskblog import app, db, bcrypt
from flaskblog.forms.forms import RegistrationForm,LoginForm
from flask_login import login_user, current_user, logout_user, login_required
import pdb

posts = [
    {
        "title": "Blog Post 1",
        "author": "Abhilash",
        "content": "This the first blog post",
        "date_posted": "17 May, 2020"
    },
    {
        "title": "Blog Post 2",
        "author": "Abhilash",
        "content": "This the second blog post",
        "date_posted": "18 May, 2020"
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Abhilash')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        password_hash_str = bcrypt.generate_password_hash(register_form.password.data).decode('utf-8')
        user = User(
                    name = register_form.username.data,
                    email = register_form.email.data,
                    password = password_hash_str
                )
        db.session.add(user)
        db.session.commit()
        flash(f'Account created. Please login!', 'success')
        return redirect(url_for('login'))
    return render_template('Register.html', title='Register', form=register_form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user, remember=login_form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsucessful. Please check username and password', 'danger')
    return render_template('Login.html', title='Login', form=login_form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')
