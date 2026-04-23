class Classroom:
    def __init__(self):
        self.students = {}

    def add_student(self, name, *grades):
        self.students[name] = list(grades)

    def average(self, name):
        if name not in self.students:
            raise ValueError(f"Student {name} not found")
        grades = self.students[name]
        return sum(grades) / len(grades) if grades else 0.0
    
    def top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda n: self.average(n))
    
    def remove_student(self, name):
        if name in self.students:
            del self.students[name]
            return f"Student {name} removed"
        else:
            return f"Student {name} not found"


c = Classroom()
c.add_student("Alice", 90, 85, 92)
c.add_student("Bob", 70, 60, 80)
print(c.average("Alice"))    # → 89.0
print(c.top_student())       # → "Alice"
print(c.remove_student("Ghost"))  # → ValueError