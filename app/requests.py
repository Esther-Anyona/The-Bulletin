from app import app
import urllib.request, json
from .models import source

NewsSource = source.NewsSource
NewsArticle = source.NewsArticle


# Get api key
api_key = app.config['API_KEY']

# News Source base url
base_url = app.config['BULLETIN_API_BASE_URL']

# Articles base url
art_url = app.config ['ARTICLES_API_BASE_URL']

def get_news():
    get_news_url = base_url.format(api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_sources = get_news_response

        if get_news_response['sources']:
            news_sources_list = get_news_response['sources']
            news_sources = process_sources(news_sources_list)

    return news_sources

def process_sources(sources_list):
    '''
    A function to process the news sources and return a list of source objects
    Args:
        sources_list: A list of dictionaries that has news sources details
    Returns: 
        news_sources: A list of source objects
        '''
    news_sources =[]
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if id:
            source_object = NewsSource(id, name, description, url, category, language, country)
            news_sources.append(source_object)

    return news_sources

def get_articles(id):
    get_article_details_url = art_url.format(id,api_key)
    print(get_article_details_url)
    with urllib.request.urlopen(get_article_details_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        source_articles = get_articles_response


        # source_articles = None

        if get_articles_response['articles']:
            source_articles_list = get_articles_response['articles']
            source_articles = process_articles(source_articles_list)
    return source_articles

def process_articles(articles):
    '''
    Function that processes the json results and returns a list of objects for the articles
    '''
    source_articles = []
    for article in articles:
        id = article.get('id')
        name = article.get('name')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')

        if url:
            article_object = NewsArticle(id, name, author, title,description, url, urlToImage, publishedAt, content)
            source_articles.append(article_object)

    return source_articles



