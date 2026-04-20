from flask import Flask, url_for, render_template, request, redirect, session, flash
from datetime import timedelta# ↓ Some session store permanent and some store temporary
from flask_sqlalchemy import SQLAlchemy # Database

app = Flask(__name__)
app.secret_key = (
    "5849854100@saesfseggeSTXs"  # Secret key is necessary to run session code
)
app.permanent_session_lifetime = timedelta(
    minutes=50
)  # The session stores data for this particular time


#TODO: Set up Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

#TODO: Create a Database
class users(db.modeL):
    _id = db.Column("id",db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.email(100))
    def __init__(self,name,email):
        self.name = name
        self.email = email    


@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # session.permanent = True -> Stores data permanent
        user = request.form["name"]
        session["user"] = user  # Save user data in session
        flash("Login Successfully!")
        return redirect(url_for("user"))
    else:
        if (
            "user" in session
        ):  # If user is in session then it redirects from login page to  user page
            flash("Already Logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user", methods=["POST","GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":  # It get the POST data from email in home.html page
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved")
        else:
            if "email" in session:
                email = session["email"]
        return render_template(
            "user.html", email = email
        )  # Redirects page login  to home with data inside it
    else:
        flash("You are not Logged in !")
        return redirect(url_for("login"))


@app.route("/logout")  # Logout from the session
def logout():
    user = session["user"]
    flash(
        f"You have been logged out! {user} "
    )  # It shows Flash message when we got logged out
    session.pop("user", None)  # It removes  the user session
    session.pop("email", None) # It removes  the email session
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()