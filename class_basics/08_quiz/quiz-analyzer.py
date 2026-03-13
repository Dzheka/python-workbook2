from student_data import student_data

NUM_PROBLEMS = 17

PROBLEM_INFO = {
    1: {"text": "Problem 1", "points": 4},
    2: {"text": "Problem 2", "points": 3},
    3: {"text": "Problem 3", "points": 4},
    4: {"text": "Problem 4", "points": 8},
    5: {"text": "Problem 5", "points": 5},
    6: {"text": "Problem 6", "points": 4},
    7: {"text": "Problem 7", "points": 10},
    8: {"text": "Problem 8", "points": 5},
    9: {"text": "Problem 9", "points": 4},
    10: {"text": "Problem 10", "points": 4},
    11: {"text": "Problem 11", "points": 5},
    12: {"text": "Problem 12", "points": 10},
    13: {"text": "Problem 13", "points": 4},
    14: {"text": "Problem 14", "points": 5},
    15: {"text": "Problem 15", "points": 6},
    16: {"text": "Problem 16", "points": 5},
    17: {"text": "Problem 17", "points": 5},
}

MAX_TOTAL = sum(info["points"] for info in PROBLEM_INFO.values())


class Student:
    def __init__(self, name, group, problems):
        self.name = name
        self.group = group
        self.problems = problems
        self.extra_points = 0

    def get_score(self):
        return sum(self.problems.values()) + self.extra_points

    def add_extra(self, points):
        self.extra_points += points

    def solved_list(self):
        return [num for num, score in self.problems.items() if score > 0]

    def failed_list(self):
        return [num for num, score in self.problems.items() if score == 0]

    def get_n(self):
        return len(self.solved_list())

    def get_v(self):
        return self.get_score()

    def get_k(self):
        if MAX_TOTAL == 0:
            return 0
        return round(self.get_score() / MAX_TOTAL * 100, 2)

    def display(self):
        print(f"Student: {self.name}")
        print(f"  Solved: {self.solved_list()}")
        print(f"  Failed: {self.failed_list()}")
        print(f"  Extra points: {self.extra_points}")
        print(f"  Total score: {self.get_score()}")
        print(f"  N={self.get_n()}, V={self.get_v()}, K={self.get_k()}%")
        print()


class Problem:
    def __init__(self, number, text, points):
        self.number = number
        self.text = text
        self.points = points
        if points <= 3:
            self.difficulty = "easy"
        elif points <= 6:
            self.difficulty = "medium"
        else:
            self.difficulty = "hard"

    def avg_score(self, students):
        scores = [s.problems.get(self.number, 0) for s in students]
        if not scores:
            return 0
        return round(sum(scores) / len(scores), 2)

    def display(self, students):
        print(f"Problem {self.number}: {self.text} | Max: {self.points} | "
              f"Difficulty: {self.difficulty} | Avg score: {self.avg_score(students)}")


if __name__ == "__main__":
    # Step 2: Create Student objects from data
    students = []
    for name, data in student_data.items():
        ratings = data["ratings"]
        problems = {}
        for i in range(1, NUM_PROBLEMS + 1):
            if i - 1 < len(ratings):
                problems[i] = ratings[i - 1]
            else:
                problems[i] = 0
        students.append(Student(name, group=1, problems=problems))

    # Step 4: Display all students
    print("=" * 50)
    print("STUDENT RESULTS")
    print("=" * 50)
    for student in students:
        student.display()

    # Task 2: Create Problem objects and display
    print("=" * 50)
    print("PROBLEM STATISTICS")
    print("=" * 50)
    problems = []
    for num, info in PROBLEM_INFO.items():
        p = Problem(num, info["text"], info["points"])
        problems.append(p)

    for p in problems:
        p.display(students)
