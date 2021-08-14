# Let's start
from flask import Flask, redirect, url_for, render_template

start = Flask(__name__)

@start.route("/")
def home():
    return render_template("index.html")

@start.route("/<name>")
def user(name):
    return render_template("user.html", sname = name, length= str(len(name)))

@start.route("/admin")
def admin():
    return redirect("user", name="Admin")


if __name__ == "__main__":
    start.run(debug=True)