from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    navn = "Mundo"
    return render_template("index.html", navn=navn)

