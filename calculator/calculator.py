import math

def calculate(expression):
    try:
        result = eval(expression)
        operation = "basic"
        if "sqrt" in expression:
            operation = "sqrt"
        elif "sin" in expression:
            operation = "sin"
        elif "cos" in expression:
            operation = "cos"
        elif "tan" in expression:
            operation = "tan"
        return result, operation
    except:
        return None, "error"
