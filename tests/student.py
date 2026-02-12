class Student:
    pass

student1 = Student()
student1.name = "student1"
student1.age = 12

student2= Student()
student2.name= "student2"
student2.age = 14

type(student1))
c(student1 = student2)
I

class Student:
     def _init (self, name, age, color):
        self.name = name
        self.age = age
        self.color =color
whiskers = Student("whiskers", 2, "orange")
=Student("mittens", 4, "black")

student:
def  _init (self, name, grade, gpa):
   self.name = name
   self.grade= grade
   self.gpa= gpa

def introduce(self):
    print(f"Hi! I'm {self.name}, in grade {self.grade}.")

def is_honor_roll(self):
    return self.gpa >= 3.5
def study(self, hours):
     boost =hours *0.05
     self .gpa= min(4.0, self.gpa + boost)
     print(f"{self.name}  studied for {hours} hours. New GPA: {self.gpa:.2f}" )
alice = Student("Alice", 10, 3.2)

alice.introduce()
print(alice.is_honor_roll())
alice.study(4)

alice.study (3)
print(alice.is_honor_roll())
