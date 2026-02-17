class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"{self.name} - GPA: {self.gpa}"

    def __eq__(self, other):
        pass

