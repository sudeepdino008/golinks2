from django.test import TestCase

from .views import normalize_path

# Create your tests here.

class InputToSystem(TestCase):

    def test_parse_url_in_correct_format(self):
        """
        validate various paths are normalized correctly
        """
        self.assertEquals('a', normalize_path('a'))
        self.assertEquals('a', normalize_path('/a'))
        self.assertEquals('a', normalize_path('a/'))
        self.assertEquals('a/b', normalize_path('a/b'))
        self.assertEquals('a/b', normalize_path('a/b/'))
        self.assertEquals('a/b', normalize_path('/a/b/'))
        self.assertEquals('a/b', normalize_path('a/b'))
        self.assertEquals('a/b', normalize_path('a/b/'))
        self.assertEquals('a/b', normalize_path('/a/b/'))
        self.assertEquals('a/b', normalize_path('/a//b//'))
        self.assertEquals('a/b/c', normalize_path('/a/b/c/'))
