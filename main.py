from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/sub', methods = ['POST', 'GET'])
def substraction():
    value1=request.args.get('A',default = 0, type = int)
    value2=request.args.get('B',default = 0, type = int)
    result=value1-value2
    return '%d \n' % result
@app.route('/add', methods = ['POST', 'GET'])
def addition():
    value1=request.args.get('A',default = 0, type = int)
    value2=request.args.get('B',default = 0, type = int)
    result=value1+value2
    return '%d \n' % result

@app.route('/mul', methods = ['POST', 'GET'])
def multiplication():
    value1=request.args.get('A',default = 0, type = int)
    value2=request.args.get('B',default = 0, type = int)
    result=value1*value2
    return '%d \n' % result

@app.route('/div', methods = ['POST', 'GET'])
def division():
    if request.method == 'POST':
        value1 = request.values.get('A', default=0, type=str)
    else:
        value1 = request.args.get('A', default=0, type=str)

    if request.method == 'GET':
        value2 = request.args.get('B', default=0, type=str)
    else:
        value2 = request.values.get('B', default=0, type=str)
    try:
        value1 = Fraction(value1)
    except ZeroDivisionError:
        return "Error: undefined value!, denominator of A value should not be a zero! \n"
    except ValueError:
        return "Error: The A value should be a numerical and it can be integer, fractional, floats! \n"
    try:
        value2 = Fraction(value2)
    except ValueError:
        return "Error: The B value should be a numerical and it can be integer, fractional, floats! \n"
    except ZeroDivisionError:
        return "Error: undefined value!, denominator of B value should not be a zero! \n"
    try: 
        result = ((value1)/(value2))
    except ZeroDivisionError:
        return "Error: undefined value!, denominator B should not be a zero! \n"
    else:
        if float(result).is_integer():
            result = int(result)
            return("Value by dividing A & B is: " '%d \n' % result)
        return("Roundup value upto three digits by dividing A & B values is: " '%.3f \n' % result)
if __name__ == "__main__":
    app.run(debug=True)