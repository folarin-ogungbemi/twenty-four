from flask import render_template
from world_barista_cup import app, db

@app.route("/")
def home():
    return render_template("index.html")