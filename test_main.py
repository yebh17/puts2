import unittest
import main

class TestCalculator(unittest.TestCase):

    def setUp(self):
    # setting up the app for testing
        main.app.test = True
        self.app = main.app.test_client()

    # Testing for substraction using integers
    def test_sub(self):
        resp = self.app.get('/sub?A=5&B=1')
        self.assertEqual(b'4 \n', resp.data)

if __name__ == '__main__':
    unittest.main()