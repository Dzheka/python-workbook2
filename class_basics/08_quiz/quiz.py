from problem import Problem
from student import Student


class Quiz:
    def __init__(self, problems, students):
        self.problems = problems
        self.students = students

    def top(self, n):
        return sorted(self.students, key=lambda s: s.get_score(), reverse=True)[:n]

    def hardest_problem(self):
        return max(self.problems, key=lambda p: p.points)

    def easiest_problem(self):
        return min(self.problems, key=lambda p: p.points)

    def average_score(self):
        return sum(s.get_score() for s in self.students) / len(self.students)

    def above_average(self):
        avg = self.average_score()
        return [s for s in self.students if s.get_score() > avg]

    def report(self):
        avg = self.average_score()
        print("=== Quiz Report ===")
        print(f"Average score: {avg:.1f}")
        print("\nTop students:")
        for i, s in enumerate(self.top(len(self.students)), 1):
            print(f"  {i}. {s.name}: {s.get_score()}")
        print("\nAll students:")
        for s in self.students:
            print(f"  {s.name}: {s.get_score()}")
