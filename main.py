 
from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)

def input_values():
    if request.method == 'POST':
        value1 = request.values.get('A', default=0, type=str)
    else:
        value1 = request.args.get('A', default=0, type=str)
    try:
        value1 = Fraction(value1)
    except ZeroDivisionError:
        return "Error: undefined value!, The denominator of A should not be a 0!, change the value of A \n"
    except ValueError:
        return "Error: The A value should be a numerical and it can be integer, fractional, floats! \n"
    if request.method == 'GET':
        value2 = request.args.get('B', default=0, type=str)
    else:
        value2 = request.values.get('B', default=0, type=str)
    try:
        value2 = Fraction(value2)
    except ZeroDivisionError:
        return "Error: undefined value!, The denominator of B should not be a 0!, change the value of B \n"
    except ValueError:
        return "Error: The B value should be a numerical and it can be integer, fractional, floats! \n"
    return value1, value2

@app.route('/', methods = ['POST', 'GET'])
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/sub', methods = ['POST', 'GET'])
def substraction():
    try:
        value1, value2 = input_values()
        result = ((value1)-(value2))
    except ValueError:
        value_error = input_values()
        return value_error
    else:
        if float(result).is_integer():
            result = int(result)
            return("Value by substracting A & B is: " '%d \n' % result)
        return("Roundup value upto three digits by substracting A & B values is: " '%.3f \n' % result)

@app.route('/add', methods = ['POST', 'GET'])
def addition():
    try:
        value1, value2 = input_values()
        result = ((value1)+(value2))
    except ValueError:
        value_error = input_values()
        return value_error
    else:
        if float(result).is_integer():
            result = int(result)
            return("Value by addition of A & B is: " '%d \n' % result)
        return("Roundup value upto three digits by addition of A & B values is: " '%.3f \n' % result)

@app.route('/mul', methods = ['POST', 'GET'])
def multiplication():
    try:
        value1, value2 = input_values()
        try:
            result = ((value1)*(value2))
        except ZeroDivisionError:
            zero_division_error = "Error: undefined value!, The value of B must not be a 0, change the value of B. \n"
            return zero_division_error
    except ValueError:
        value_error = input_values()
        return value_error
    else:
        if float(result).is_integer():
            result = int(result)
            return("Value by multiplying A & B is: " '%d \n' % result)
        return("Roundup value upto three digits by multiplying A & B values is: " '%.3f \n' % result)

@app.route('/div', methods = ['POST', 'GET'])
def division():
    try:
        value1, value2 = input_values()
        try:
            result = ((value1)/(value2))
        except ZeroDivisionError:
            zero_division_error = "Error: undefined value!, The value of B must not be a 0, change the value of B. \n"
            return zero_division_error
    except ValueError:
        value_error = input_values()
        return value_error
    else:
        if float(result).is_integer():
            result = int(result)
            return("Value by dividing A & B is: " '%d \n' % result)
        return("Roundup value upto three digits by dividing A & B values is: " '%.3f \n' % result)

if __name__ == "__main__":
    app.run(debug=True)