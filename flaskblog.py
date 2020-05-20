from flask import Flask, render_template, url_for, redirect, flash
from forms.forms import RegistrationForm, LoginForm
import pdb

app = Flask(__name__)
app.config['SECRET_KEY']='33e5b8deeb6b8413ce14adf16063176c'

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
