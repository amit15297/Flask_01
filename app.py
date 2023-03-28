from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world1():
    return "<h1>Hello, World! 1</h1>"

@app.route("/test")
def test():
    a = 5+4
    return "This is Test function {}".format(a)

@app.route("/test2/test2")
def test2():
    data = request.args.get('x')
    return "This is my Input Data from URL {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
