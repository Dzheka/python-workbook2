from quiz_data import student_data

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
        return f"{self.name} (Group{self.group}) - Score: {self.get_score()}"
    
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
        return sorted(self.students, key=lambda s: s.get_score(), reverse=True)[:n]

    def hardest_problem(self):
        return min(self.problems, key=lambda p: sum(1 for s in self.students if s.problems[p.number] > 0))

    def easiest_problem(self):
        return max(self.problems, key=lambda p: sum(1 for s in self.students if s.problems[p.number] > 0))

    def average_score(self):
        return sum(s.get_score() for s in self.students) / len(self.students)

    def above_average(self):
        avg = self.average_score()
        return [s for s in self.students if s.get_score() > avg]
    
    def report(self):
        print("=== QUIZ REPORT ===")
        print("\n-- Students Ranking --")
        rank = 1
        for s in self.top(len(self.students)):
            print(f"{rank}. {s.name} | Score: {s.get_score()} | Group: {s.group}")
            rank += 1

        print("\n-- Problems Overview --")
        for p in self.problems:
            solved_count = 0
            for s in self.students:
                if s.problems[p.number] > 0:
                    solved_count += 1
            avg_score = p.avg_score(self.students)
            print(f"Problem {p.number}: {p.text}")
            print(f"   Difficulty: {p.difficulty}")
            print(f"   Solved by: {solved_count} students")
            print(f"   Avg score: {avg_score:.2f}")

        print("\n-- Summary --")
        print(f"Overall average score: {self.average_score():.2f}")
        print("Top 3 students:", ", ".join([s.name for s in self.top(3)]))
        print("Above average:", ", ".join([s.name for s in self.above_average()]))



