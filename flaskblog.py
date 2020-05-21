from flask import Flask, render_template, url_for, redirect, flash
from datetime import datetime
from forms.forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
import pdb

app = Flask(__name__)
app.config['SECRET_KEY']='33e5b8deeb6b8413ce14adf16063176c'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='post_author', lazy=True)

    def __repr__(self):
        return f"User(name: '{self.name}', email: '{self.email}', image_file: '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post(author: '{self.author}', title: '{self.title}', content: '{self.content}', date_posted: '{self.date_posted}')"


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
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        flash(f'Account acctivated for {register_form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('Register.html', title='Register', form=register_form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit:
        if login_form.email.data == 'abhilash.palem@shuttl.com' and login_form.password.data == 'abhi':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsucessful. Please check username and password', 'danger')
    return render_template('Login.html', title='Login', form=login_form)

if __name__ == '__main__' :
    app.run(debug=True)
