# The 4 Pillars of Object-Oriented Programming

> You already know **classes**, **objects**, and **dunder methods**.
> Now let's understand the **philosophy** behind it all.

---

```
                      OOP
        ┌────────┬────────┬────────┐
        │        │        │        │
   Encapsulation │   Polymorphism  │
             Inheritance      Abstraction
```

---

## Pillar 1 — Encapsulation

**One sentence:** Hide the details, expose only what's needed.

**Real life:** You drive a car — you use the steering wheel and pedals. You don't manually inject fuel into cylinders. The engine is **encapsulated** behind a simple interface.

### The Problem

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

timur = Student("Timur", 89)
timur.grade = -500       # nobody stopped us
timur.grade = 999999     # impossible grade, but Python allows it
```

### Access Types: Public, Protected, Private

Python uses naming conventions to signal access levels:

```
┌──────────┬───────────────┬──────────────────────────────────────────┐
│  Type    │  Syntax       │  Who can access?                         │
├──────────┼───────────────┼──────────────────────────────────────────┤
│ Public   │  self.name    │  Everyone — from anywhere                │
│ Protected│  self._name   │  Class + children (by convention only)   │
│ Private  │  self.__name  │  Only inside the class itself            │
└──────────┴───────────────┴──────────────────────────────────────────┘
```

### Example — All Three Types

```python
class Student:
    def __init__(self, name, group, grade):
        self.name = name            # public  — everyone can see the name
        self._group = group         # protected — "please don't touch from outside"
        self.__grade = grade        # private — only this class can access

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        if not 0 <= value <= 100:
            print("Grade must be between 0 and 100")
            return
        self.__grade = value

    def __str__(self):
        return f"{self.name} (Group {self._group}) — Grade: {self.__grade}"


shahrom = Student("Shahrom", 1, 83)

# Public — works everywhere
print(shahrom.name)          # Shahrom

# Protected — works, but convention says "don't do this"
print(shahrom._group)        # 1 — works but shouldn't be used outside

# Private — blocked
# print(shahrom.__grade)     # AttributeError!
print(shahrom.grade)         # 83 — through @property

# Setter with validation
shahrom.grade = 90           # works
shahrom.grade = -500         # Grade must be between 0 and 100
shahrom.grade = 999          # Grade must be between 0 and 100
print(shahrom)               # Shahrom (Group 1) — Grade: 90
```

### Quick Comparison

```python
class QuizResult:
    def __init__(self, student_name, score, answers):
        self.student_name = student_name    # public — name is fine to show
        self._answers = answers             # protected — internal detail
        self.__score = score                # private — can't be changed directly

    @property
    def score(self):
        return self.__score

    def add_bonus(self, points):
        if 0 < points <= 10:
            self.__score += points
            print(f"{self.student_name} got +{points} bonus -> {self.__score}")


nizar = QuizResult("Nizar", 72, [4, 3, 2, 8, 5])
print(nizar.student_name)    # Nizar           — public
print(nizar.score)           # 72              — property
nizar.add_bonus(5)           # Nizar got +5 bonus -> 77
# nizar.__score = 100        # Can't cheat!
# nizar._answers             # Works but "please don't"
```

### Name Mangling — What Actually Happens

```python
timur = Student("Timur", 1, 89)

# Python secretly renames __grade to _Student__grade
print(timur._Student__grade)   # 89 — technically works, but NEVER do this

# This is called "name mangling" — it's a safety mechanism, not a wall
# In Python we trust developers to follow conventions
```

### When to Use What

```
┌────────────────────────────────────────────────────────┐
│  self.name        PUBLIC       Always safe to access   │
│  self._name       PROTECTED    Children can use it     │
│  self.__name      PRIVATE      Only inside this class  │
├────────────────────────────────────────────────────────┤
│  Rule of thumb:                                        │
│  - Start with public                                   │
│  - Make it protected if only subclasses need it        │
│  - Make it private if nobody should touch it directly  │
└────────────────────────────────────────────────────────┘
```

---

## Pillar 2 — Inheritance

**One sentence:** Create new classes based on existing ones — reuse code, extend behavior.

**Real life:** A quiz has **students**. Some students attend regularly, some don't. Instead of writing two completely separate classes, we write a base class and extend it.

### Simplest Example — No Inheritance (The Problem)

```python
class RegularStudent:
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def greet(self):
        print(f"Hi, I'm {self.name} from group {self.group}")

    def study(self):
        print(f"{self.name} is studying")


class ExchangeStudent:
    def __init__(self, name, group):        # same code
        self.name = name
        self.group = group

    def greet(self):                         # same code
        print(f"Hi, I'm {self.name} from group {self.group}")

    def study(self):                         # same code
        print(f"{self.name} is studying")

    def translate(self):                     # only this is new
        print(f"{self.name} is translating notes")
```

We copied 90% of the code. Now imagine 5 types of students — nightmare.

### Simplest Inheritance — The Fix

```python
class Student:                              # Parent class
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def greet(self):
        print(f"Hi, I'm {self.name} from group {self.group}")

    def study(self):
        print(f"{self.name} is studying")


class ExchangeStudent(Student):             # Inherits EVERYTHING from Student
    def translate(self):                     # Adds its own method
        print(f"{self.name} is translating notes")


ahmadjon = Student("Ahmadjon", 1)
ahmadjon.greet()     # Hi, I'm Ahmadjon from group 1
ahmadjon.study()     # Ahmadjon is studying

behruz = ExchangeStudent("Behruz", 1)
behruz.greet()       # Hi, I'm Behruz from group 1    — inherited!
behruz.study()       # Behruz is studying              — inherited!
behruz.translate()   # Behruz is translating notes     — own method
```

That's it. `ExchangeStudent(Student)` means "take everything from Student and add more."

### Adding `__init__` in a Child — `super()`

What if the child needs extra attributes?

```python
class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def __str__(self):
        return f"{self.name} (Group {self.group})"


class OnlineStudent(Student):
    def __init__(self, name, group, timezone):
        super().__init__(name, group)       # call parent's __init__
        self.timezone = timezone            # add own attribute

    def __str__(self):
        return f"{self.name} (Group {self.group}, TZ: {self.timezone})"


abubakr = Student("Abubakr", 1)
najmiya = OnlineStudent("Najmiya", 1, "UTC+5")

print(abubakr)   # Abubakr (Group 1)
print(najmiya)    # Najmiya (Group 1, TZ: UTC+5)
```

`super()` = "call the parent's version of this method"

```
Student.__init__(name, group)        — sets name & group
    ^
    super().__init__(name, group)     — OnlineStudent calls parent first
    ^
OnlineStudent.__init__(name, group, timezone)  — then adds timezone
```

### Real Example — Quiz System

```python
class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def status(self):
        return "Active"

    def __str__(self):
        return f"{self.name} — Avg: {self.average():.1f} [{self.status()}]"


class TopStudent(Student):
    """Students with average above 80"""
    def status(self):
        return "Top Student"

    def mentor(self, other):
        print(f"{self.name} is helping {other.name}")


class AbsentStudent(Student):
    """Students with many missed classes"""
    def __init__(self, name, group, missed_classes):
        super().__init__(name, group)
        self.missed_classes = missed_classes

    def status(self):
        return f"Absent ({self.missed_classes} missed)"

    def __str__(self):
        return f"{self.name} — Avg: {self.average():.1f} [{self.status()}]"


# Regular students
otabek = Student("Otabek", 1)
otabek.add_score(48)

maryam = Student("Maryam", 1)
maryam.add_score(28)

# Top students
timur = TopStudent("Timur", 1)
timur.add_score(89)

shahrom = TopStudent("Shahrom", 1)
shahrom.add_score(83)

# Absent students
ismoiljon = AbsentStudent("Ismoiljon", 1, missed_classes=12)
muhammadjon = AbsentStudent("Muhammadjon", 1, missed_classes=15)

# Everything just works
everyone = [timur, shahrom, otabek, maryam, ismoiljon, muhammadjon]
for s in everyone:
    print(s)

# Timur — Avg: 89.0 [Top Student]
# Shahrom — Avg: 83.0 [Top Student]
# Otabek — Avg: 48.0 [Active]
# Maryam — Avg: 28.0 [Active]
# Ismoiljon — Avg: 0.0 [Absent (12 missed)]
# Muhammadjon — Avg: 0.0 [Absent (15 missed)]

# Top student can mentor others
timur.mentor(maryam)    # Timur is helping Maryam
shahrom.mentor(otabek)  # Shahrom is helping Otabek
```

### What Gets Inherited

```python
# Check with isinstance
print(isinstance(timur, TopStudent))  # True
print(isinstance(timur, Student))     # True — TopStudent IS a Student
print(isinstance(otabek, TopStudent)) # False

# Check inheritance chain
print(TopStudent.__bases__)           # (<class 'Student'>,)
```

### Key Ideas

```
┌──────────────────────────────┐
│         INHERITANCE          │
├──────────────────────────────┤
│  class Child(Parent)         │
│  super().__init__(...)       │
│                              │
│  - No copy-paste             │
│  - Shared logic in parent    │
│  - Unique logic in children  │
│  - Easy to add new types     │
└──────────────────────────────┘
```

---

## Pillar 3 — Polymorphism

**One sentence:** Same method name, different behavior depending on the object.

**Real life:** The teacher says "submit your homework." Timur submits code on GitHub. Maryam sends a PDF. Amir writes on paper. The **command is the same**, the **result is different**.

### Basic Example

```python
class Student:
    def __init__(self, name):
        self.name = name

    def submit(self):
        raise NotImplementedError("Subclasses must implement submit()")


class CoderStudent(Student):
    def submit(self):
        return f"{self.name} pushed code to GitHub"


class WriterStudent(Student):
    def submit(self):
        return f"{self.name} uploaded a PDF to Google Drive"


class PresenterStudent(Student):
    def submit(self):
        return f"{self.name} gave a live presentation"
```

### The Magic — One Loop, Different Behaviors

```python
students = [
    CoderStudent("Timur"),
    WriterStudent("Maryam"),
    PresenterStudent("Abdul-Aziz"),
    CoderStudent("Nizar"),
    WriterStudent("Gulsum"),
]

for student in students:
    print(student.submit())

# Timur pushed code to GitHub
# Maryam uploaded a PDF to Google Drive
# Abdul-Aziz gave a live presentation
# Nizar pushed code to GitHub
# Gulsum uploaded a PDF to Google Drive
```

We call the **same method** `.submit()` on every object. Each responds **in its own way**.

### Adding New Types — Zero Changes Elsewhere

```python
class GroupStudent(Student):
    def __init__(self, name, partner):
        super().__init__(name)
        self.partner = partner

    def submit(self):
        return f"{self.name} & {self.partner} submitted a group project"

# Works instantly everywhere:
students.append(GroupStudent("Abubakr", "Ahmadjon"))
for student in students:
    print(student.submit())
```

### Real Example — Grading System

```python
class Assignment:
    def __init__(self, student_name):
        self.student_name = student_name

    def calculate_grade(self):
        raise NotImplementedError

    def feedback(self):
        grade = self.calculate_grade()
        if grade >= 80:
            return f"{self.student_name}: {grade}% — Excellent"
        elif grade >= 50:
            return f"{self.student_name}: {grade}% — Keep going"
        else:
            return f"{self.student_name}: {grade}% — Needs more practice"


class QuizAssignment(Assignment):
    def __init__(self, student_name, correct, total):
        super().__init__(student_name)
        self.correct = correct
        self.total = total

    def calculate_grade(self):
        return round(self.correct / self.total * 100)


class ProjectAssignment(Assignment):
    def __init__(self, student_name, code_quality, creativity, docs):
        super().__init__(student_name)
        self.code_quality = code_quality    # 0-40
        self.creativity = creativity        # 0-30
        self.docs = docs                    # 0-30

    def calculate_grade(self):
        return self.code_quality + self.creativity + self.docs


class AttendanceAssignment(Assignment):
    def __init__(self, student_name, classes_attended, total_classes):
        super().__init__(student_name)
        self.attended = classes_attended
        self.total = total_classes

    def calculate_grade(self):
        return round(self.attended / self.total * 100)


# Different grading formulas, same interface
assignments = [
    QuizAssignment("Shahrom", 14, 17),
    ProjectAssignment("Ilyos", code_quality=35, creativity=20, docs=10),
    AttendanceAssignment("Ismoiljon", 3, 15),
    QuizAssignment("Behruz", 12, 17),
    AttendanceAssignment("Muhammadjon", 0, 15),
]

for a in assignments:
    print(a.feedback())

# Shahrom: 82% — Excellent
# Ilyos: 65% — Keep going
# Ismoiljon: 20% — Needs more practice
# Behruz: 71% — Keep going
# Muhammadjon: 0% — Needs more practice
```

### Polymorphism + Dunder Methods

You already know this. Dunder methods **are** polymorphism:

```python
# __str__ — same function, different result
print(timur)          # Timur — Avg: 89.0 [Top Student]
print(ismoiljon)      # Ismoiljon — Avg: 0.0 [Absent (12 missed)]

# __len__ — different classes, same call
len([1, 2, 3])        # 3     — list's __len__
len("hello")          # 5     — string's __len__
len(my_playlist)      # 12    — your custom __len__

# __add__ — different classes, same operator
3 + 5                 # int's __add__
"hi" + "!"            # str's __add__
wallet1 + wallet2     # your custom __add__
```

### Key Ideas

```
┌──────────────────────────────┐
│        POLYMORPHISM          │
├──────────────────────────────┤
│  Same method name            │
│  Different behavior          │
│                              │
│  Parent defines interface    │
│  Children implement details  │
│                              │
│  - Write code for "Student"  │
│    not for each type         │
│  - Easy to add new types     │
│  - Dunder methods are this   │
└──────────────────────────────┘
```

---

## Pillar 4 — Abstraction

**One sentence:** Show only what matters, hide the complexity.

**Real life:** When you submit homework, you click "Submit". You don't think about file encoding, server connections, or database writes. That complexity is **abstracted away**.

### Abstraction vs Encapsulation

```
Encapsulation = HOW we hide  (__, @property)
Abstraction   = WHAT we hide (unnecessary details)

Encapsulation is the tool.
Abstraction is the goal.
```

### Example — Classroom Management System

```python
# Bad: Teacher must do everything manually
class ClassroomBad:
    def load_students_from_file(self, filepath):
        ...
    def parse_csv_line(self, line):
        ...
    def validate_student_data(self, data):
        ...
    def create_student_object(self, name, group, scores):
        ...
    def calculate_individual_average(self, student):
        ...
    def sort_by_score(self, students):
        ...
    def format_report_line(self, student, rank):
        ...
    def write_report_to_file(self, filepath):
        ...

# To use it — you need to call 8 methods in the right order
```

```python
# Good: Simple interface, complexity hidden inside
class Classroom:
    def __init__(self, name):
        self.name = name
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)
        print(f"{student.name} joined {self.name}")

    def remove_absent_students(self, max_absences):
        before = len(self.__students)
        self.__students = [s for s in self.__students if s.missed_classes <= max_absences]
        removed = before - len(self.__students)
        print(f"Removed {removed} students with >{max_absences} absences")

    def top(self, n):
        ranked = sorted(self.__students, key=lambda s: s.average(), reverse=True)
        return ranked[:n]

    def report(self):
        self.__print_header()
        self.__print_students()
        self.__print_stats()

    # --- All complexity hidden below ---
    def __print_header(self):
        print(f"\n{'='*40}")
        print(f"  Report: {self.name}")
        print(f"{'='*40}")

    def __print_students(self):
        ranked = sorted(self.__students, key=lambda s: s.average(), reverse=True)
        for i, s in enumerate(ranked, 1):
            print(f"  {i}. {s}")

    def __print_stats(self):
        if not self.__students:
            return
        avg = sum(s.average() for s in self.__students) / len(self.__students)
        print(f"\n  Students: {len(self.__students)}")
        print(f"  Class Average: {avg:.1f}")
        print(f"{'='*40}")


# Teacher uses 3 simple methods — doesn't care how it works inside
room = Classroom("Python 101")
room.add_student(timur)
room.add_student(shahrom)
room.add_student(ismoiljon)
room.report()
```

### Real Example — Grade Book

```python
class GradeBook:
    def __init__(self):
        self.__records = {}

    def record(self, student_name, assignment, grade):
        """One simple method to record a grade"""
        if student_name not in self.__records:
            self.__records[student_name] = {}
        self.__validate_grade(grade)
        self.__records[student_name][assignment] = grade
        print(f"Recorded: {student_name} — {assignment} = {grade}")

    def get_average(self, student_name):
        """One simple method to get average"""
        grades = self.__records.get(student_name, {})
        if not grades:
            return 0
        return sum(grades.values()) / len(grades)

    def failing_students(self, threshold=50):
        """One simple method to find who's struggling"""
        return [name for name in self.__records
                if self.get_average(name) < threshold]

    # Hidden complexity
    def __validate_grade(self, grade):
        if not 0 <= grade <= 100:
            raise ValueError(f"Invalid grade: {grade}")


book = GradeBook()
book.record("Timur", "Quiz 1", 89)
book.record("Timur", "Quiz 2", 92)
book.record("Maftunbek", "Quiz 1", 39)
book.record("Abduvozit", "Quiz 1", 12)

print(book.get_average("Timur"))          # 90.5
print(book.failing_students())            # ['Maftunbek', 'Abduvozit']
```

### Abstract Base Classes (Bonus)

Python can **force** children to implement certain methods:

```python
from abc import ABC, abstractmethod

class Assignment(ABC):                    # Can't create directly
    @abstractmethod
    def calculate_grade(self):
        pass

    @abstractmethod
    def feedback(self):
        pass


# assignment = Assignment()              # TypeError! Can't instantiate abstract class

class QuizAssignment(Assignment):
    def __init__(self, correct, total):
        self.correct = correct
        self.total = total

    def calculate_grade(self):            # Must implement — otherwise error
        return round(self.correct / self.total * 100)

    def feedback(self):                   # Must implement
        grade = self.calculate_grade()
        return f"Quiz: {grade}%"


quiz = QuizAssignment(14, 17)             # Works — all abstract methods implemented
```

### Key Ideas

```
┌──────────────────────────────┐
│        ABSTRACTION           │
├──────────────────────────────┤
│  Simple public interface     │
│  Complex private internals   │
│                              │
│  User calls: report()        │
│  Class handles: sort,        │
│    format, calculate, print  │
│                              │
│  - Easy to use               │
│  - Safe to change internals  │
│  - Focus on WHAT not HOW     │
└──────────────────────────────┘
```

---

## Summary — All 4 Pillars Together

```
┌──────────────────────────────────────────────────────┐
│                    OOP PILLARS                        │
├──────────────┬───────────────────────────────────────┤
│              │                                       │
│ ENCAPSULATION│  Protect data with __ and @property   │
│              │  public / _protected / __private       │
│              │                                       │
├──────────────┼───────────────────────────────────────┤
│              │                                       │
│ INHERITANCE  │  Child classes reuse parent code      │
│              │  class Child(Parent) + super()         │
│              │                                       │
├──────────────┼───────────────────────────────────────┤
│              │                                       │
│ POLYMORPHISM │  Same method, different behavior      │
│              │  .submit() works for all types         │
│              │                                       │
├──────────────┼───────────────────────────────────────┤
│              │                                       │
│ ABSTRACTION  │  Hide complexity, expose simplicity   │
│              │  .report() hides 5 private methods     │
│              │                                       │
└──────────────┴───────────────────────────────────────┘
```

### How They All Connect — One Final Example

```python
from abc import ABC, abstractmethod


# ABSTRACTION — defines what a class member must do
class ClassMember(ABC):
    def __init__(self, name, group):
        self.name = name                   # PUBLIC
        self._group = group                # PROTECTED
        self.__attendance = 0              # PRIVATE (ENCAPSULATION)

    @property
    def attendance(self):                  # ENCAPSULATION — safe access
        return self.__attendance

    def attend(self):
        self.__attendance += 1

    @abstractmethod
    def role(self):                        # ABSTRACTION — children must define
        pass

    def __str__(self):
        return f"{self.name} [{self.role()}] — {self.__attendance} classes"


# INHERITANCE — reuse ClassMember code
class ActiveStudent(ClassMember):
    def __init__(self, name, group, score):
        super().__init__(name, group)
        self.score = score

    def role(self):                        # POLYMORPHISM — own implementation
        if self.score >= 80:
            return "Top"
        elif self.score >= 50:
            return "Active"
        else:
            return "Struggling"


class AbsentStudent(ClassMember):          # INHERITANCE
    def __init__(self, name, group, missed):
        super().__init__(name, group)
        self.missed = missed

    def role(self):                        # POLYMORPHISM — different behavior
        return f"Absent ({self.missed} missed)"


class TeachingAssistant(ClassMember):      # INHERITANCE
    def role(self):                        # POLYMORPHISM
        return "TA"


# All 4 pillars working together
members = [
    ActiveStudent("Timur", 1, 89),
    ActiveStudent("Shahrom", 1, 83),
    ActiveStudent("Amir", 1, 44),
    ActiveStudent("Maftunbek", 1, 39),
    AbsentStudent("Ismoiljon", 1, missed=12),
    AbsentStudent("Muhammadjon", 1, missed=15),
    TeachingAssistant("Habibulloh", 1),
]

# POLYMORPHISM — same loop, different results
for m in members:
    print(m)

# Timur [Top] — 0 classes
# Shahrom [Top] — 0 classes
# Amir [Struggling] — 0 classes
# Maftunbek [Struggling] — 0 classes
# Ismoiljon [Absent (12 missed)] — 0 classes
# Muhammadjon [Absent (15 missed)] — 0 classes
# Habibulloh [TA] — 0 classes
```

---

## Quick Reference Card

| Pillar | Question to Ask | Python Tool |
|--------|----------------|-------------|
| **Encapsulation** | "Is my data safe?" | `self.x`, `self._x`, `self.__x`, `@property` |
| **Inheritance** | "Am I repeating code?" | `class Child(Parent)`, `super()` |
| **Polymorphism** | "Can I use one interface?" | Method overriding, dunders |
| **Abstraction** | "Is my class easy to use?" | Private methods, `ABC`, `@abstractmethod` |
