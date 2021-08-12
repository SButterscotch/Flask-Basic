# Let's start
from flask import Flask, redirect, url_for

site = Flask(__name__)

@site.route("/")
def home():
    return "This is the Home Page"

@site.route("/<name>")
def user(name):
    return f"Hello {name}!"

@site.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    site.run()