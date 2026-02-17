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
        total = 0
        count = 0
        for s in students:
            total += s.problems.get(self.number, 0)
            count += 1
        return total / count if count > 0 else 0

    def to_dict(self):
        return {
            "number": self.number,
            "text": self.text,
            "points": self.points,
            "difficulty": self.difficulty
        }


class Student:
    def __init__(self, name, group, problems, extra_points=0):
        self.name = name
        self.group = group
        self.problems = problems
        self.extra_points = extra_points

    def get_score(self):
        return sum(self.problems.values()) + self.extra_points

    def add_extra(self, points):
        self.extra_points += points

    def solved_list(self):
        solved = []
        for num, score in self.problems.items():
            if score > 0:
                solved.append(num)
        return solved

    def failed_list(self):
        failed = []
        for num, score in self.problems.items():
            if score == 0:
                failed.append(num)
        return failed

    def __str__(self):
        return f"{self.name} (Group {self.group}) - Score: {self.get_score()}"

    def get_n(self):
        return len(self.solved_list())

    def get_v(self):
        return sum(self.problems.values())

    def get_k(self):
        return self.get_score()


class Quiz:
    def __init__(self, problems, students):
        self.problems = problems
        self.students = students

    def top(self, n):
        sorted_students = sorted(self.students, key=lambda s: s.get_score(), reverse=True)
        return sorted_students[:n]

    def hardest_problem(self):
        hardest = None
        min_solved = None
        for p in self.problems:
            solved_count = 0
            for s in self.students:
                if s.problems.get(p.number, 0) > 0:
                    solved_count += 1
            if min_solved is None or solved_count < min_solved:
                min_solved = solved_count
                hardest = p
        return hardest

    def easiest_problem(self):
        easiest = None
        max_solved = None
        for p in self.problems:
            solved_count = 0
            for s in self.students:
                if s.problems.get(p.number, 0) > 0:
                    solved_count += 1
            if max_solved is None or solved_count > max_solved:
                max_solved = solved_count
                easiest = p
        return easiest

    def average_score(self):
        total = 0
        for s in self.students:
            total += s.get_score()
        return total / len(self.students)

    def above_average(self):
        avg = self.average_score()
        result = []
        for s in self.students:
            if s.get_score() > avg:
                result.append(s)
        return result

    def report(self):
        pass