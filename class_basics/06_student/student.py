class Student:
    def __init__(self, name, student_id,) :
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self,grade):
        self.grades.append(grade)
        print(f"Added grade: {grade}")

    def calculate_average(self):
        if not len(self.grades):
            return  0.0
        return sum(self.grades) / len(self.grades)



student = Student("Alice", "S123")
student.add_grade(85)    # Added grade: 85
student.add_grade(92)    # Added grade: 92
student.add_grade(78)    # Added grade: 78
print(student.calculate_average())  # 85.0