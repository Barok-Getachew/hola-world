# Create your testsres here.
from urllib import response
from django.test import SimpleTestCase

class Simple_test(SimpleTestCase) :
    def test_home_page_status(self) :
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 404)
    def test_about_page_status(self) :
        response = self.client.get('/About')
        self.assertEqual(response.status_code, 404)

