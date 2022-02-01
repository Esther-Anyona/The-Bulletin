from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news, get_articles

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    source = get_news()
    title = 'Welcome to The Bulletin'
    return render_template('index.html', title = title, source = source)

@main.route('/source/<id>')
def source(id):
    '''
    View sources page function that returns the articles from the source data
    '''
    article = get_articles(id)
    title = 'Flash News'
    return render_template('source.html', title = title, article = article, id=id)