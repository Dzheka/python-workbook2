
class Employee:
    def __init__(self, name, salary, department):
        self.name       = name
        self.salary     = salary
        self.department = department

    def get_info(self):
        print(f"Employee: {self.name}, Department: {self.department}, Salary: ${self.salary}")

    def get_annual_bonus(self):
        return self.salary * 0.1


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)

    def get_annual_bonus(self):
        return self.salary * 0.2

    def manage_team(self):
        print(f"{self.name} is managing the {self.department} team")



class Developer(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)

    def get_annual_bonus(self):
        return self.salary * 0.15

    def code_review(self):
        print(f"{self.name} is reviewing code")



employee  = Employee("John",  50000, "HR")
manager   = Manager("Sarah",  80000, "Engineering")
developer = Developer("Mike", 70000, "Engineering")

employee.get_info()
print(f"John's annual bonus: ${employee.get_annual_bonus()}")

print()
manager.get_info()
print(f"Sarah's annual bonus: ${manager.get_annual_bonus()}")
manager.manage_team()

print()
developer.get_info()
print(f"Mike's annual bonus: ${developer.get_annual_bonus()}")
developer.code_review()
