from flask import Flask, request

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
    value1=request.args.get('A',default = 0, type = int)
    value2=request.args.get('B',default = 0, type = int)
    result=value1/value2
    return '%d \n' % result

if __name__ == "__main__":
    app.run()

