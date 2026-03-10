class Classroom:
    def __init__(self):
        self.students = {}

    def add_student(self, name, *grades):
        self.students[name] = list(grades)

    def average(self, name):
        grades = self.students[name]
        return sum(grades) / len(grades)

    def top_student(self):
        return max(self.students, key=lambda name: self.average(name))

    def remove_student(self, name):
        if name not in self.students:
            raise ValueError(f"{name} not found")
        del self.students[name]
