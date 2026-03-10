class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def get_info(self):
        print(f"Employee: {self.name}, Department: {self.department}, Salary: ${self.salary}")

    def get_annual_bonus(self):
        return self.salary * 0.1


class Manager(Employee):
    def get_annual_bonus(self):
        return self.salary * 0.2

    def manage_team(self):
        print(f"{self.name} is managing the {self.department} team")


class Developer(Employee):
    def get_annual_bonus(self):
        return self.salary * 0.15

    def code_review(self):
        print(f"{self.name} is reviewing code")
