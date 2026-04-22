#^ https://youtu.be/I0Zu-Jtp898

from flask import Flask, render_template, request, redirect , abort
from templates.models import db, StudentModel


app = Flask(__name__)

# TODO: Set up Database
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///students.db"  # ^ It creates the database name students.db in an instance file
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    def create_table():  # * function for create database
        db.create_all()

@app.route("/create", methods=["GET", "POST"])
def create():  # * function for create
    if request.method == "GET":
        return render_template("create.html")
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        gender = request.form["gender"]
        hobbies = ",".join(request.form.getlist("hobbies"))

        students = StudentModel(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            gender=gender,
            hobbies=hobbies,

        )  #! It inserts all the retrieved values into the database
        db.session.add(students)
        db.session.commit()
        return redirect("/")

@app.route("/", methods=["GET"])
def RetriveList():
    students = StudentModel.query.all()   #! It stores all the data here and pass in index.html page
    return render_template('index.html',students=students)

#* update method filterations 
@app.route("/<int:id>/update", methods=["GET", "POST"])
def update(id):
    students = StudentModel.query.filter_by(id=id).first()
    if request.method == "POST":
        if students:
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            email = request.form.get("email")
            password = request.form.get("password")
            gender = request.form.get("gender")  # Use .get() to avoid KeyError
            hobbies = ",".join(request.form.getlist("hobbies"))

            # Update the student object
            students.first_name = first_name
            students.last_name = last_name
            students.email = email
            students.password = password
            students.gender = gender
            students.hobbies = hobbies

            db.session.commit()
            return redirect("/")
        return f"Student with ID:{id} does not exist"
    return render_template("update.html", students=students)

#* Delete method filterations 
@app.route("/<int:id>/delete", methods=["GET","POST"])  
def delete(id):
    students = StudentModel.query.filter_by(id=id).first()
    if not students:
        return abort(404)
    if request.method == "POST":
            db.session.delete(students)
            db.session.commit()
            return redirect("/")

    return render_template('delete.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)