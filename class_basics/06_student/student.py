class Student():
    def __init__(self,name,student_id,grades=[]) -> None:
        self.name = name
        self.student_id = student_id
        self.grades = grades


    def add_grade(self,grade):
        self.grades.append(grade)
        print(f'Added grade: {grade}')

    def calculate_average(self):
        grade_total = 0
        for grade in self.grades:
            grade_total += grade
        return grade_total / len(self.grades)

student = Student("Alice", "S123")
student.add_grade(85)    # Added grade: 85
student.add_grade(92)    # Added grade: 92
student.add_grade(78)    # Added grade: 78
print(student.calculate_average())  # 85.0
