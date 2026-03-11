from quiz_data import student_data

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
        
    def display(self):
        print(f"Student: {self.name}")
        print(f"Solved problems: {self.solved_list()}")
        print(f"Failed problems: {self.failed_list()}")
        print(f"Extra points: {self.extra_points}")
        print(f"Total score: {self.get_score()}")
        print("-" * 30)

    def get_n(self):
        return len(self.solved_list())
    
    def get_v(self):
        return sum(self.problems.values())
    
    def get_k(self):
        return self.get_score()
    
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
        scores = []
        for s in students:
            if self.number in s.problems:
                scores.append(s.problems[self.number])
            else:
                scores.append(0)
        
        if len(scores) > 0:
            avg = sum(scores) / len(scores)
            return avg
        else:
            return 0
        
    def display(self, students):
        avg = self.avg_score(students)
        print(f"Problem {self.number}: {self.text}")
        print(f"Points: {self.points}, Difficulty: {self.difficulty}")
        print(f"Average score: {avg:.2f}")
        print("-"*30)

students = []
for name, info in student_data.items():
    ratings = info.get("ratings", [])
    problems = {}
    for i in range(17):
        if i < len(ratings):
            problems[i+1] = ratings[i]
        else:
            problems[i+1] = 0

    student = Student(name, group=1, problems=problems)
    students.append(student)

students[0].add_extra(5)

for s in students:
    s.display()
    print(f"N = {s.get_n()}, V = {s.get_n()}, k = {s.get_k()}")
    print("="*40)