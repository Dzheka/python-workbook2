class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def get_info(self):
        return f"Employee: {self.name}, Department: {self.department}, Salary: ${self.salary}"
    
    def get_annual_bonus(self):
        return self.salary * 0.1
    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)

    def get_annual_bonus(self):
        return self.salary * 0.2
    
    def manage_team(self):
        return f"{self.name} is managing the {self.department} team"
    
class Developer(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)

    def get_annual_bonus(self):
        return self.salary * 0.15
    
    def code_review(self):
        return f"{self.name} is reviewing code"
    
# Create different types of employees
employee = Employee("John", 50000, "HR")
manager = Manager("Sarah", 80000, "Engineering")
developer = Developer("Mike", 70000, "Engineering")

# Show employee information and bonuses
print(employee.get_info())   # Employee: John, Department: HR, Salary: $50000
print(f"John's annual bonus: ${employee.get_annual_bonus()}")  # John's annual bonus: $5000.0

print(manager.get_info())    # Employee: Sarah, Department: Engineering, Salary: $80000
print(f"Sarah's annual bonus: ${manager.get_annual_bonus()}")  # Sarah's annual bonus: $16000.0
print(manager.manage_team()) # Sarah is managing the Engineering team

print(developer.get_info())  # Employee: Mike, Department: Engineering, Salary: $70000
print(f"Mike's annual bonus: ${developer.get_annual_bonus()}")  # Mike's annual bonus: $10500.0
print(developer.code_review())  # Mike is reviewing code