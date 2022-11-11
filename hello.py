from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/japan/tokyo")
def hello_tokyo():
    return "<p>Hello, tokyo in Japan!</p>"

@app.route("/japan/nara")
def hello_nara():
    return "<p>Hello, nara in Japan!</p>"

@app.route("/japan/saitama")
def hello_saitama():
    return "<p>Hello, saitama in Japan!</p>"

