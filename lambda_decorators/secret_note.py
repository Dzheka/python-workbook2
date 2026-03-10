def make_bold(func):
    def wrapper():
        result = func()
        return f"*** {result} ***"
    return wrapper