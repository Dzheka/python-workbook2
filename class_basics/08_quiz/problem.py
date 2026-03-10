class Problem:
    def __init__(self, number, text, points):
        self.number = number
        self.text = text
        self.points = points

    @property
    def difficulty(self):
        if self.points <= 3:
            return "easy"
        elif self.points <= 6:
            return "medium"
        else:
            return "hard"

    def avg_score(self, students):
        scores = [s.problems.get(self.number, 0) for s in students]
        return sum(scores) / len(scores)

    def to_dict(self):
        return {"number": self.number, "text": self.text, "points": self.points}

    def display(self):
        print(f"Problem {self.number}: {self.text} ({self.points} pts, {self.difficulty})")
