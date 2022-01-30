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