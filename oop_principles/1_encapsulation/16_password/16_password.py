class Password:


    def __init__(self, password):
        self._validate(password)
        self._password = password


    def _validate(self, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if not any(c.isupper() for c in password):
            raise ValueError("Password must contain at least one uppercase letter")

        if not any(c.islower() for c in password):
            raise ValueError("Password must contain at least one lowercase letter")

        if not any(c.isdigit() for c in password):
            raise ValueError("Password must contain at least one digit")

        if not any(c in "!@#$%^&*" for c in password):
            raise ValueError("Password must contain at least one special character (!@#$%^&*)")


    def get_strength(self):
        if len(self._password) >= 12:
            return "Strong"
        return "Medium"


    def check_password(self, input_password):
        return self._password == input_password


    def change_password(self, old_password, new_password):
        if not self.check_password(old_password):
            raise ValueError("Old password is incorrect")
        self._validate(new_password)
        self._password = new_password



password = Password("MyP@ssw0rd123")
print(password.get_strength())

print(password.check_password("MyP@ssw0rd123"))
print(password.check_password("wrong"))

password.change_password("MyP@ssw0rd123", "NewP@ss2024!")
print(password.check_password("NewP@ss2024!"))


try:
    weak = Password("123")
except ValueError as e:
    print(e)

try:
    weak = Password("password")
except ValueError as e:
    print(e)


medium = Password("Passw0rd!")
strong = Password("MyStr0ng!Pass")
print(medium.get_strength())
print(strong.get_strength())

