from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/japan")
def hello_japan():
    return "<p>Hello, Japan!</p>"

@app.route("/america")
def hello_america():
    return "<p>Hello, America!</p>"
