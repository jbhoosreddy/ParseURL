import unittest
from ParseURL import *


class TestParsing(unittest.TestCase):

    def test_url1(self):
        url = 'https://www.google.com:80/login?username=johndoe&password=nanananananananabatman'
        parser = ParseURL(url)
        parser.parse()
        self.assertEqual(parser.parsed_url.get_attr('scheme'), "https")
        self.assertEqual(parser.parsed_url.get_attr('query'), {'username': 'johndoe', 'password': 'nanananananananabatman'})
        self.assertEqual(parser.parsed_url.get_attr('fragment'), "")

    def test_url2(self):
        url = 'https://www.google.com:80/login#dashboard'
        parser = ParseURL(url)
        parser.parse()
        self.assertEqual(parser.parsed_url.get_attr('scheme'), "https")
        self.assertEqual(parser.parsed_url.get_attr('fragment'), "dashboard")
        self.assertEqual(parser.parsed_url.get_attr('query'), {})

    def test_url3(self):
        url = 'https://www.quora.com/notifications'
        parser = ParseURL(url)
        parser.parse()
        self.assertEqual(parser.parsed_url.get_attr('scheme'), "https")
        self.assertEqual(parser.parsed_url.get_attr('path'), "/notifications")
        self.assertEqual(parser.parsed_url.get_attr('netloc'), "www.quora.com")

    def test_url4(self):
        url = 'HTTP://www.Python.org/doc/#'
        parser = ParseURL(url)
        parser.parse()
        self.assertEqual(parser.parsed_url.get_attr('scheme'), "http")
        self.assertEqual(parser.parsed_url.get_attr('netloc'), "www.Python.org")

    def test_url5(self):
        url = 'http://www.ics.uci.edu/pub/ietf/uri/#Related'
        parser = ParseURL(url)
        parser.parse()
        self.assertEqual(parser.parsed_url.get_attr('scheme'), "http")
        self.assertEqual(parser.parsed_url.get_attr('netloc'), "www.ics.uci.edu")
        self.assertEqual(parser.parsed_url.get_attr('path'), "/pub/ietf/uri/")
        self.assertEqual(parser.parsed_url.get_attr('fragment'), "Related")

    def test_url6(self):
        url = 'http://username:password@www.my_site.com'
        parser = ParseURL(url)
        parser.parse()
        self.assertEqual(parser.parsed_url.get_attr('scheme'), "http")
        self.assertEqual(parser.parsed_url.get_attr('netloc'), "www.my_site.com")
        self.assertEqual(parser.parsed_url.get_attr('username'), "username")
        self.assertEqual(parser.parsed_url.get_attr('password'), "password")


if "__name__" == "__main__":
    unittest.main()