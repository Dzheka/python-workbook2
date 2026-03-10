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

    @property
    def n(self):
        return len(self.solved_list())

    @property
    def v(self):
        total = sum(self.problems.values())
        possible = sum(self.problems.keys())
        if possible == 0:
            return 0
        return total / possible

    @property
    def k(self):
        return self.extra_points

    def display(self):
        print(f"{self.name} | Score: {self.get_score()} | Solved: {self.n}/17")

    def __str__(self):
        return f"{self.name} (Group {self.group}) - Score: {self.get_score()}"
