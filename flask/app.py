from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# SGPA calculation
@app.route("/sgpa", methods=["GET", "POST"])
def calculate_sgpa():
    sgpa = None
    if request.method == "POST":
        total_points = 0
        total_credits = 0
        f = int(request.form.get("subjects"))

        for i in range(f):
            grade = request.form.get(f"grade{i}")
            credit = int(request.form.get(f"credit{i}"))

            match grade.upper():
                case "O":
                    gp = 10
                case "A+":
                    gp = 9
                case "A":
                    gp = 8
                case "B+":
                    gp = 7
                case "B":
                    gp = 6
                case "C":
                    gp = 5
                case "U":
                    gp = 0
                case _:
                    gp = 0

            total_points += gp * credit
            total_credits += credit

        sgpa = round(total_points / total_credits, 2)

    return render_template("sgpa.html", sgpa=sgpa)

# CGPA calculation
@app.route("/cgpa", methods=["GET", "POST"])
def calculate_cgpa():
    cgpa = None
    if request.method == "POST":
        total_points = 0
        total_credits = 0
        n = int(request.form.get("semesters"))

        for i in range(n):
            sgpa = float(request.form.get(f"sgpa{i}"))
            credits = int(request.form.get(f"credits{i}"))
            total_points += sgpa * credits
            total_credits += credits

        cgpa = round(total_points / total_credits, 2)

    return render_template("cgpa.html", cgpa=cgpa)

if __name__ == "__main__":
    app.run(debug=True)
