from logging import debug
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/<name>")
def home(name):
    return render_template(
        "index.html", content=["Ved", "Kayaan", "Tux"]
    )  #! Live argument and parameter that calls in HTML page.


if __name__ == "__main__":

    app.run(debug=True)
