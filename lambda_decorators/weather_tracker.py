def check_auth(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@check_auth
def view_grades(user):
    print(f"Viewing grades for {user}: A+")