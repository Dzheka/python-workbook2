from quiz_data import student_data

class Problem:
    def __init__(self, number, text, points):
        self.number = number
        self.text = text
        self.points = points

        if self.points <= 3:
            self.difficulty = "easy"
        elif self.points <= 6:
            self.difficulty = "medium"
        else:
            self.difficulty = "hard"
    
    def avgscore(self, students):
        avg = sum()