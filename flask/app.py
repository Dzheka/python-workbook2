from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

students_data = {
    "Abdul-Aziz": 77, "Abdullo": 47, "Abubakr": 59,
    "Ahmadjon": 69, "Amir": 44, "Behruz": 69,
    "Habibulloh": 51, "Ilyos": 64, "Maftunbek": 39,
    "Maryam": 28, "Mubarro": 22, "Najmiya": 60,
    "Otabek": 48, "Shahrom": 83, "Habibullo": 63,
    "Rukhshona": 31, "Osiya": 69, "Bakhtiyor": 32,
    "Muhammadjon": 0, "Timur": 89, "Gulsum": 36,
    "Rayhona": 39, "Abduvozit": 12, "Ismoiljon": 0,
    "Nizar": 72,
}

def get_status(score):
    if score >= 80:
        return "Excellent"
    elif score >= 50:
        return "Good"
    elif score >= 1:
        return "Needs improvement"
    else:
        return "No data"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/students")
def students():
    sorted_students = sorted(students_data.items(), key=lambda x: x[1], reverse=True)
    return render_template("students.html", students=sorted_students)


@app.route("/student/<name>")
def student(name):

    if name not in students_data:
        return render_template("student.html", error="Student not found"), 404

    score = students_data[name]
    status = get_status(score)

    return render_template("student.html", name=name, score=score, status=status)


@app.route("/api/students")
def api_students():
    return jsonify(students_data)


@app.route("/api/student/<name>")
def api_student(name):

    if name not in students_data:
        return jsonify({"error": "Student not found"}), 404

    score = students_data[name]

    return jsonify({
        "name": name,
        "score": score,
        "status": get_status(score)
    })


@app.route("/add", methods=["GET", "POST"])
def add():

    error = None

    if request.method == "POST":

        name = request.form.get("name")
        score = request.form.get("score")

        if not name:
            error = "Name cannot be empty"

        elif name in students_data:
            error = "Student already exists"

        else:
            try:
                score = int(score)

                if score < 0 or score > 100:
                    error = "Score must be between 0 and 100"
                else:
                    students_data[name] = score
                    return redirect(url_for("students"))

            except:
                error = "Score must be a number"

    return render_template("add.html", error=error)


if __name__ == "__main__":
    app.run(debug=True)
