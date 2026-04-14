from logging import debug
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World"


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


@app.route("/admin")
def admin():
    return redirect(url_for("user",name="Admin!")) #! Return route with Admin! argument  


if __name__ == "__main__":

    app.run(debug=True)
