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
    # Testing for addition using integers
    def test_add(self):
        resp = self.app.get('/add?A=1&B=5')
        self.assertEqual(b'6 \n', resp.data)
    # Testing for multiplication using integers
    def test_mul(self):
        resp = self.app.get('/mul?A=1&B=5')
        self.assertEqual(b'5 \n', resp.data)

if __name__ == '__main__':
    unittest.main()