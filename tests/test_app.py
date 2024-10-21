import unittest
from lundpy import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World from Flask!')

if __name__ == "__main__":
    unittest.main()
