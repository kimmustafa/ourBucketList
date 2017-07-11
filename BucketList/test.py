from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_signup_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertTrue('BucketList', response.data)
if __name__ == '__main__':
    unittest.main()