from flask import Flask, request, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Tanvi", "course": "Computer Engineering"},
    {"id": 2, "name": "Rahul", "course": "Information Technology"}
]

@app.route("/")
def home():
    return """
    <h1>Student Management System</h1>
    <p>DevOps Mini Project</p>
    <p>Open /students to view student records.</p>
    """

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/students", methods=["POST"])
def add_student():
    data = request.json
    student = {
        "id": len(students) + 1,
        "name": data["name"],
        "course": data["course"]
    }
    students.append(student)
    return jsonify(student), 201

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    global students
    students = [student for student in students if student["id"] != student_id]
    return jsonify({"message": "Student deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)