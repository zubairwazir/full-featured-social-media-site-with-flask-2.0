from flask import render_template, url_for, redirect, flash
from app import app
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post


posts = [
    {
        'author': 'Zubair Ahmad',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Jan 15, 2022'
    },
    {
        'author': 'Alec Deleany',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Jan 15, 2022'
    }
]

@app.get("/")
@app.get("/home")
def home():
    return render_template('home.html', posts=posts)


@app.get("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'admin':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
