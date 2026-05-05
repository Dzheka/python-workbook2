class Classroom:

    def __init__(self):
        self.students = {}


    def add_student(self, name, *grades):
        self.students[name] = list(grades)


    def average(self, name):
        grades = self.students[name]
        return sum(grades) / len(grades)


    def top_student(self):
        best_name  = None
        best_avg   = -1

        for name in self.students:
            avg = self.average(name)
            if avg > best_avg:
                best_avg  = avg
                best_name = name

        return best_name


    def remove_student(self, name):
        if name not in self.students:
            raise ValueError(f"{name} not found")
        del self.students[name]



c = Classroom()
c.add_student("Alice", 90, 85, 92)
c.add_student("Bob", 70, 60, 80)

print(c.average("Alice"))
print(c.top_student())
c.remove_student("Ghost")
