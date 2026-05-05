

def log_transaction (func):
    def wrapper(amount):
        print("Transaction started")
        result = func(amount)
        print(f"Transaction finished: {result}")
        return result
    return wrapper

@log_transaction
def transfer(amount):
     return amount

transfer(500)
