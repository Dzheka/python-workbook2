from flask import Flask,render_template,jsonify,request,redirect

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



@app.route("/")
def main():
    return render_template("/main_page.html")


@app.route("/about")
def about():
    return render_template("/about.html")


@app.route('/students')
def list_students():
    search_query = request.args.get("search", "").strip().lower()

    if search_query:
        filtered_students = {
            name: score for name, score in students_data.items() 
            if search_query in name.lower()
        }
    else:
        filtered_students = students_data

    sorted_students = dict(sorted(filtered_students.items(), key=lambda item: item[1], reverse=True))
    return render_template("students.html", students=sorted_students, search_query=search_query)

@app.route("/student/<name>")
def student_detail(name):
    name  = name.title() 

    if name not in students_data:
        return render_template("/404.html")
    
    score = students_data[name]
    
    if score >= 80:
        result = 'Excellent'
    elif 50 <= score <= 79:
        result = "Good"
    elif 1 <= score <= 49:
        result = "Needs improvement"
    else:
        result = "No data"
    
    return render_template("student.html", name=name, score=score, result=result)


@app.route("/api/students")
def all_students():
    return jsonify(students_data)

@app.route("/api/student/<name>")
def one_student(name):
    name = name.title()
    if name not in students_data:
        return jsonify({"error": "Student not found"}), 404
    score = students_data[name]
    if score >= 80:
        feedback = 'Excellent'
    elif 50 <= score <= 79:
        feedback = "Good"
    elif 1 <= score <= 49:
        feedback = "Needs improvement"
    else:
        feedback = "No data"

    fresult = {
        "name": name,
        "score": score,
        "status": feedback

    }
    return jsonify(fresult)


@app.route("/add", methods=["GET", "POST"])
def add_student():
    error = None
    
    if request.method == "POST":
        name = request.form.get("name", "").strip().title()
        score_str = request.form.get("score")

        if not name:
            error = "Error: Name cannot be empty."
        elif name in students_data:
            error = f"Error: '{name}' is already in the scoreboard."
        else:
            try:
                score = int(score_str)
                if 0 <= score <= 100:
                    students_data[name] = score
                    return redirect("/students") 
                else:
                    error = "Error: Score must be between 0 and 100."
            except (ValueError, TypeError):
                error = "Error: Please enter a valid numerical score."

    return render_template("add.html", error=error)
        


if __name__ == "__main__":
    app.run(debug=True)