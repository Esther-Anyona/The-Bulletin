import unittest
from app.models import NewsSource

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behavior of the NewsSource class
    '''
    def setUp(self):
        '''
        Set up method to run before every test
        '''

        self.new_source = NewsSource('abc-news', 'ABC News', 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.', 'https://abcnews.go.com', 'general', 'en', 'us' )
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, NewsSource))

