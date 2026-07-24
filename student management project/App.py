from flask import Flask, render_template, request, redirect
app = Flask(__name__)

students = []

@app.route('/')
def home():
    search = request.args.get("search", "").lower()

    if search:
        filtered_students = [
            student for student in students
            if search in student["id"].lower()
            or search in student["name"].lower()
            or search in student["course"].lower()
        ]
    else:
        filtered_students = students

    return render_template("Index.html", students=filtered_students)

@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        student = {
            "id": request.form["id"],
            "name": request.form["name"],
            "course": request.form["course"]
        }
        students.append(student)
        return redirect("/")
    return render_template("Add.html")

@app.route('/edit/<int:index>', methods=["GET", "POST"])
def edit(index):
    if request.method == "POST":
        students[index]["id"] = request.form["id"]
        students[index]["name"] = request.form["name"]
        students[index]["course"] = request.form["course"]
        return redirect("/")
    return render_template("Edit.html", student=students[index])

@app.route('/delete/<int:index>')
def delete(index):
    students.pop(index)
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)