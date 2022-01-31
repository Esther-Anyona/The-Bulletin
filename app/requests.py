from app import app
import urllib.request, json
from .models import source

NewsSource = source.NewsSource

# Get api key
api_key = app.config['API_KEY']

# News Source base url
base_url = app.config['BULLETIN_API_BASE_URL']

def get_news(sources):
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
        source_object = NewsSource(id, name, description, url, category, language, country)
        news_sources.append(source_object)

return news_sources
