# Let's start
from flask import Flask, redirect, url_for, render_template

start = Flask(__name__)

@start.route("/")
def home():
    return render_template("index.html")
            

@start.route("/<name>")
def user(name):
    return f"<h1> Hi {name} <h1>"

@start.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    start.run()