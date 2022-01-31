from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    source = get_news()
    title = 'Welcome to The Bulletin'
    return render_template('index.html', title = title, source = source)