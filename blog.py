
""" Script that runs a flask application"""
from flask import Flask, render_template
app = Flask(__name__)


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
    return render_template('about.html')


if __name__ == '__main__':
    app.run()