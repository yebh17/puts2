import unittest
import main

class TestCalculator(unittest.TestCase):

    def setUp(self):
    # setting up the app for testing
        main.app.test = True
        self.app = main.app.test_client()

    # Testing for addition using integers
    def test_add(self):
        resp = self.app.get('/add?A=1&B=5')
        self.assertEqual(b'6 \n', resp.data)

if __name__ == '__main__':
    unittest.main()