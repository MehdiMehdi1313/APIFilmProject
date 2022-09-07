from flask import Flask

app = Flask(__name__)

@app.route("/")
def movie():
    return "<p>Movies list</p>"