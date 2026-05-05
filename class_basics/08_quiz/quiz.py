from quiz_data import student_data


class Student():
    def __init__(self, name, group,problems, extra_points = 0) -> None:
        self.name = name
        self.group = group
        self.problems = problems
        self.extra_points = extra_points


    def get_score(self):
        total_score = 0
        for i in student_data[self.name]['ratings']:
            total_score += i
        return total_score + self.extra_points

    def add_extra(self,points):
        self.extra_points += points
        return self.extra_points

    def solved_list(self):
        s_list = []
        for i,mark in enumerate(student_data[self.name]['ratings'], start=1):
            if mark > 0:
                s_list.append(i)
            else:
                continue
        return s_list

    def failed_list(self):
        f_list = []
        for i,mark in enumerate(student_data[self.name]['ratings'], start=1):
            if mark == 0:
                f_list.append(i)
            else:
                continue
        return f_list

    def display(self):
        print(
            f"Student Name: {self.name}\n"
            f"Solved problems: {self.solved_list()}\n"
            f"Unsolved problems: {self.failed_list()}\n"
            f"Extra points: {self.extra_points}\n"
            f"Total score: {self.get_score()}\n" +
            "-" * 40
        )

    def N(self):
        s_count = 0
        for mark in student_data[self.name]["ratings"]:
            if mark > 0:
                s_count += 1
            else:
                continue
        return s_count

    def V(self):
        return sum(i for i in student_data[self.name]['ratings'])

    def K(self):
        total = len(self.problems)
        return ((self.N())/ total) if total > 0 else 0


class Problem():
    def __init__(self, number, text,points,difficulty= None) -> None:
        self.number = number
        self.text = text
        self.points = points
        if difficulty == None:
            if self.points >= 1 and self.points <= 3:
                self.difficulty = "easy"
            elif self.points >=4 and self.points <= 6:
                self.difficulty = "medium"
            elif self.points >= 7:
                self.difficulty = "hard"

    def avg_score(self,students):
        points_total = 0
        points_num = 0
        for student in students:
            score = student.problems.get(self.number, 0)
            points_total += score
            points_num += 1

        return points_total / points_num if points_num > 0 else 0

    def display(self, students):
        print(
            f"Problem {self.number}\n"
            f"Description: {self.text}\n"
            f"Max points: {self.points}\n"
            f"Difficulty: {self.difficulty}\n"
            f"Average score: {self.avg_score(students):.2f}\n"
            + "-" * 40
        )


#Creating Student objects

students = []

max_problems = max(len(data["ratings"]) for data in student_data.values())

for name, data in student_data.items():
    ratings = data["ratings"]

    if ratings:
        problems = {i + 1: ratings[i] for i in range(len(ratings))}
    else:
        problems = {i + 1: 0 for i in range(max_problems)}

    student = Student(
        name=name,
        group="A",
        problems=problems
    )

    students.append(student)

#Displaying all students

for student in students:
    student.display()

#N,V,K

for student in students:
    print(f"Student: {student.name}")
    print(f"N (solved problems): {student.N()}")
    print(f"V (total score): {student.V()}")
    print(f"K (efficiency): {student.K():.2f}")
    print("-" * 40)


#Creating Problems objects

problems = []

for i in range(1, 18):
    problems.append(
        Problem(
            number=i,
            text=f"Quiz problem {i}",
            points=5   # example: medium difficulty
        )
    )

#Average score for each student/printing all
for problem in problems:
    problem.display(students)