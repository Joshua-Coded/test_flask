from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '1bce43da0fa199def6acc2f7dcfb6d2e'

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

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)