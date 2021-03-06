from crypt import methods
from flask import Flask, render_template, url_for, redirect, flash
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = '025a5be698d19717aa1f74f29587b39d'  # import secrets -> secrets.token_hex(16)
db = SQLAlchemy(app)


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


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
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


if "__main__" == __name__:
    app.run(debug=True)