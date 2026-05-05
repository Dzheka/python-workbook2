class Classroom:
    def __init__(self):
        self.students = {}

    def add_student(self,name,*grade):
        if not grade:
            self.students[name] = 0.0
        else:
            self.students[name] = sum(grade) / len(grade)

    def average(self,name):
        if name in self.students:
            return self.students[name]
        return f"Not in the list"

    def top_student(self):
        if not self.students:
            return "No students"
        return max(self.students, key=self.students.get)

    def remove_student(self, name):
        if name in self.students:
            del self.students[name]
        else:
            raise ValueError("Student not found")


