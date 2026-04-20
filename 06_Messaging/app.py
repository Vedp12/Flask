from flask import Flask, url_for, render_template, request, redirect, session, flash

# ↓ Some session store permanent and some store temporary
from datetime import timedelta


app = Flask(__name__)
app.secret_key = (
    "5849854100@saesfseggeSTXs"  # Secret key is necessary to run session code
)
app.permanent_session_lifetime = timedelta(
    days=5
)  # The session stores data for this particular time


@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # session.permanent = True -> Stores data permanent
        user_main = request.form["name"]
        session["user"] = user_main  # Save user data in session
        flash("Login Successfully!")
        return redirect(url_for("user"))
    else:
        if (
            "user" in session
        ):  # If user is in session then it redirects from login page to  user page
            flash("Already Logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user_main = session["user"]

        return render_template(
            "user.html", user_main = user_main
        )  # Redirects page login  to home with data inside it
    else:
        flash("You are not Logged in !")
        return redirect(url_for("login"))


@app.route("/logout")  # Logout from the session
def logout():
    user_main = session["user"]
    flash(
        f"You have been logged out! {user_main} "
    )  # It shows Flash message when we got logged out
    session.pop("user", None)  # It removes the session
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
