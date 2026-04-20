from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", context="Testing")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
