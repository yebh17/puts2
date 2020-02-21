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
    # Testing for division
    def test_div(self):

        # Testing for division using integers.
        resp = self.app.get('/div?A=24&B=12')
        self.assertEqual(b'Value by dividing A & B is: 2 \n', resp.data)

        # Testing for division for rational values.
        resp = self.app.get('/div?A=1/3&B=2/3')
        self.assertEqual(b'Roundup value upto three digits by dividing A & B values is: 0.500 \n', resp.data)

        # Testing for division for integer values.
        resp = self.app.get('/div?A=11&B=7')
        self.assertEqual(b'Roundup value upto three digits by dividing A & B values is: 1.571 \n', resp.data)

        # Testing for division for both float values.
        resp = self.app.get('/div?A=0.2&B=0.3')
        self.assertEqual(b'Roundup value upto three digits by dividing A & B values is: 0.667 \n', resp.data)

if __name__ == '__main__':
    unittest.main()