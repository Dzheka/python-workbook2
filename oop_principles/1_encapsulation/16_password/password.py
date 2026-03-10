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
            raise ValueError("Password must contain at least one special character")

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
