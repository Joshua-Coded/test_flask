from flask import render_template, url_for, flash, redirect
from blog import app, db, bcrypt
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post


posts = [
    {
        'author': 'Joshua Alana',
        'title': 'Blog Post',
        'content': 'First Post Content',
        'date_posted': 'February 23 2024'
        },
        {
        'author': 'Alana',
        'title': 'Twitter Post',
        'content': 'First Post Content',
        'date_posted': 'February 23 2024'
        }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created you are now able to login! <!><!><!> {form.username.data}!', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '12345':
            flash('You have Successfully Logged In', 'success')
            return redirect(url_for('home'))
        else:
            flash("Log In Failed. Please Check Email and Password", "danger")
    return render_template('login.html', title='Login', form=form)

