# Let's start
from flask import Flask, redirect, url_for

start = Flask(__name__)

@start.route("/")
def home():
    return (f"<h1> This is the home page <h1>\n <h2> I'll try Implementing firebase <h2> \n",
            f"<h3> This is gonna be a gateay to Django <h3>")

@start.route("/<name>")
def user(name):
    return f"<h1> Hi {name} <h1>"

@start.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    start.run()