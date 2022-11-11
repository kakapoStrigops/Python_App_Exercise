from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/japan/<city>")
def hello_japan(city):
    return f"<p>Hello, { city } in Japan!</p>"
