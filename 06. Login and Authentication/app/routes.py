from flask import render_template, url_for, redirect, flash
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from flask_login import  login_user, logout_user, current_user


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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registered Successfully! Please Login Now.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful! Please check Email and Password.', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))