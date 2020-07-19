import unittest
import main

class TestCalculator(unittest.TestCase):

    def setUp(self):
    # setting up the app for testing
        main.app.test = True
        self.app = main.app.test_client()

    #Testing handler for methods responses
    def test_handler(self):
        resp = self.app.get('/')
        self.assertEqual(b'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n', resp.data)

        resp = self.app.post('/')
        self.assertEqual(b'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n', resp.data)

    # Testing for addition using integers
    def test_add(self):

        #Testing wether POST method is satisfying to return the result.
        resp = self.app.post('/add', data = dict(A = '2', B = '5'))
        self.assertEqual(b'7 \n', resp.data)

        # Testing for addition using integrals.
        resp = self.app.get('/add?A=1&B=5')
        self.assertEqual(b'6 \n', resp.data)

        # Testing for addition using integrals.
        resp = self.app.get('/add?A=-1&B=-5')
        self.assertEqual(b'-6 \n', resp.data)

        #Testing for addition of fractional values.
        resp = self.app.get('/add?A=1/3&B=2/4')
        self.assertEqual(b'0.833 \n', resp.data)

        #Testing for A value as integer and B value as float.
        resp = self.app.get('/add?A=11&B=-3.174')
        self.assertEqual(b'7.826 \n', resp.data)

        #Testing for A value as float and B value as integer.
        resp = self.app.get('/add?A=5.123&B=13')
        self.assertEqual(b'18.123 \n', resp.data)      

        # Testing for addition for both float values.
        resp = self.app.get('/add?A=0.2&B=0.3')
        self.assertEqual(b'0.500 \n', resp.data)

        #Testing for A value as integer and B value as fraction.
        resp = self.app.get('/add?A=-5&B=2/3')
        self.assertEqual(b'-4.333 \n', resp.data)

        #Testing for A value as fraction and B value as integer.
        resp = self.app.get('/add?A=2/3&B=7')
        self.assertEqual(b'7.667 \n', resp.data)

        #Testing for A's value as fraction and, denominator is a zero and numerator is an integer.
        resp = self.app.get('/add?A=2/0&B=7')
        self.assertEqual(b'Error: undefined value!, The denominator of A should not be a 0!, change the value of A \n', resp.data) 

         #Testing for B's value as fraction and, denominator is a zero and numerator is an integer.
        resp = self.app.get('/add?A=2&B=7/0')
        self.assertEqual(b'Error: undefined value!, The denominator of B should not be a 0!, change the value of B \n', resp.data) 

        #Testing for A as an non numerical case.
        resp = self.app.get('/add?A=hej&B=21')
        self.assertEqual(b'Error: The A value should be a numerical and it can be integer, fractional, floats! \n', resp.data)

        #Testing for B as an non numerical case.
        resp = self.app.get('/add?A=21&B=hello')
        self.assertEqual(b'Error: The B value should be a numerical and it can be integer, fractional, floats! \n', resp.data)

    # Testing for substraction using integers
    def test_sub(self):

        #Testing wether POST method is satisfying to return the result.
        resp = self.app.post('/sub', data = dict(A = '2', B = '5'))
        self.assertEqual(b'-3 \n', resp.data)

        # Testing for substracting using integrals.
        resp = self.app.get('/sub?A=1&B=5')
        self.assertEqual(b'-4 \n', resp.data)

        #Testing for substracting fractional values.
        resp = self.app.get('/sub?A=1/3&B=2/3')
        self.assertEqual(b'-0.333 \n', resp.data)

        #Testing for A value as integer and B value as float.
        resp = self.app.get('/sub?A=-11&B=3.174')
        self.assertEqual(b'-14.174 \n', resp.data)

        #Testing for A value as float and B value as integer.
        resp = self.app.get('/sub?A=5.123&B=13')
        self.assertEqual(b'-7.877 \n', resp.data)      

        # Testing for substraction for both float values.
        resp = self.app.get('/sub?A=0.2&B=-0.3')
        self.assertEqual(b'0.500 \n', resp.data)

        #Testing for A value as integer and B value as fraction.
        resp = self.app.get('/sub?A=5&B=2/3')
        self.assertEqual(b'4.333 \n', resp.data)

        #Testing for A value as fraction and B value as integer.
        resp = self.app.get('/sub?A=2/3&B=7')
        self.assertEqual(b'-6.333 \n', resp.data)

        #Testing for A's value as fraction and, denominator is a zero and numerator is an integer.
        resp = self.app.get('/sub?A=2/0&B=7')
        self.assertEqual(b'Error: undefined value!, The denominator of A should not be a 0!, change the value of A \n', resp.data) 

         #Testing for B's value as fraction and, denominator is a zero and numerator is an integer.
        resp = self.app.get('/sub?A=2&B=7/0')
        self.assertEqual(b'Error: undefined value!, The denominator of B should not be a 0!, change the value of B \n', resp.data) 

        #Testing for A as an non numerical case.
        resp = self.app.get('/sub?A=hej&B=21')
        self.assertEqual(b'Error: The A value should be a numerical and it can be integer, fractional, floats! \n', resp.data)

        #Testing for B as an non numerical case.
        resp = self.app.get('/sub?A=21&B=hello')
        self.assertEqual(b'Error: The B value should be a numerical and it can be integer, fractional, floats! \n', resp.data)

    # Testing for multiplication using integers
    def test_mul(self):

        #Testing wether POST method is satisfying to return the result.
        resp = self.app.post('/mul', data = dict(A = '2', B = '5'))
        self.assertEqual(b'10 \n', resp.data)

        # Testing for multiplication using integrals.
        resp = self.app.get('/mul?A=1&B=5')
        self.assertEqual(b'5 \n', resp.data)

        #Testing for multiplying for fractional values.
        resp = self.app.get('/mul?A=1/3&B=2/3')
        self.assertEqual(b'0.222 \n', resp.data)

        #Testing for A value as integer and B value as float.
        resp = self.app.get('/mul?A=11&B=3.174')
        self.assertEqual(b'34.914 \n', resp.data)

        #Testing for A value as float and B value as integer.
        resp = self.app.get('/mul?A=5.123&B=-13')
        self.assertEqual(b'-66.599 \n', resp.data)      

        # Testing for multiplication for both float values.
        resp = self.app.get('/mul?A=0.2&B=0.3')
        self.assertEqual(b'0.060 \n', resp.data)

        #Testing for A value as integer and B value as fraction.
        resp = self.app.get('/mul?A=5&B=2/3')
        self.assertEqual(b'3.333 \n', resp.data)

        #Testing for A value as fraction and B value as integer.
        resp = self.app.get('/mul?A=-2/3&B=7')
        self.assertEqual(b'-4.667 \n', resp.data)

        #Testing for A's value as fraction and, denominator is a zero and numerator is an integer.
        resp = self.app.get('/mul?A=2/0&B=4/3')
        self.assertEqual(b'Error: undefined value!, The denominator of A should not be a 0!, change the value of A \n', resp.data) 

         #Testing for B's value asfraction and, denominator is a zero and numerator is an integer.
        resp = self.app.get('/mul?A=4/3&B=7/0')
        self.assertEqual(b'Error: undefined value!, The denominator of B should not be a 0!, change the value of B \n', resp.data) 

        #Testing for A as an non numerical case.
        resp = self.app.get('/mul?A=hej&B=21')
        self.assertEqual(b'Error: The A value should be a numerical and it can be integer, fractional, floats! \n', resp.data)

        #Testing for B as an non numerical case.
        resp = self.app.get('/mul?A=21&B=hello')
        self.assertEqual(b'Error: The B value should be a numerical and it can be integer, fractional, floats! \n', resp.data)

    # Testing for division
    def test_div(self):

        #Testing wether POST method is satisfying to return the result.
        resp = self.app.post('/div', data = dict(A = '2', B = '5'))
        self.assertEqual(b'0.400 \n', resp.data)

        # Testing for division using integrals.
        resp = self.app.get('/div?A=24&B=12')
        self.assertEqual(b'2 \n', resp.data)

        # Testing for division for fractional values.
        resp = self.app.get('/div?A=1/3&B=2/3')
        self.assertEqual(b'0.500 \n', resp.data)

        # Testing for division for integer values.
        resp = self.app.get('/div?A=-11&B=7')
        self.assertEqual(b'-1.571 \n', resp.data)

        #Testing for A value as integer and B value as float.
        resp = self.app.get('/div?A=11&B=3.174')
        self.assertEqual(b'3.466 \n', resp.data)

        #Testing for A value as float and B value as integer.
        resp = self.app.get('/div?A=5.123&B=-13')
        self.assertEqual(b'-0.394 \n', resp.data)      

        # Testing for division for both float values.
        resp = self.app.get('/div?A=0.2&B=0.3')
        self.assertEqual(b'0.667 \n', resp.data)

        #Testing for A value as integer and B value as fraction.
        resp = self.app.get('/div?A=5&B=2/3')
        self.assertEqual(b'7.500 \n', resp.data)

        #Testing for A value as fraction and B value as integer.
        resp = self.app.get('/div?A=2/3&B=7')
        self.assertEqual(b'0.095 \n', resp.data)

        #Testing for A's value as fraction and, denominator is a zero and numerator is an integer.
        resp = self.app.get('/div?A=2/0&B=7/3')
        self.assertEqual(b'Error: undefined value!, The denominator of A should not be a 0!, change the value of A \n', resp.data) 

         #Testing for B's value as fraction and, denominator is a zero and numerator is an integer.
        resp = self.app.get('/div?A=7&B=7/0')
        self.assertEqual(b'Error: undefined value!, The denominator of B should not be a 0!, change the value of B \n', resp.data) 

        #Testing for A as integer and B is zero.
        resp = self.app.get('/div?A=2&B=0')
        self.assertEqual(b'Error: undefined value!, The value of B must not be a 0, change the value of B. \n', resp.data)

        #Testing for A as an non numerical case.
        resp = self.app.get('/div?A=hej&B=21')
        self.assertEqual(b'Error: The A value should be a numerical and it can be integer, fractional, floats! \n', resp.data)

        #Testing for B as an non numerical case.
        resp = self.app.get('/div?A=21&B=hello')
        self.assertEqual(b'Error: The B value should be a numerical and it can be integer, fractional, floats! \n', resp.data)

if __name__ == '__main__':
    unittest.main()