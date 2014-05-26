from mock.mock import Mock
from base import GAETestCase
from web import home

class HomeTests(GAETestCase):
    def test_sucesso(self):
        handler = Mock()
        home.index(handler)
        handler.assert_called_once_with('/templates/home.html')