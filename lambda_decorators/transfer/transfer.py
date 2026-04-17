def log_transaction(func):
    def wrapper(amount):
        print("Transaction started")
        result = func(amount)
        print("Transaction finished:", result)
        return result
    return wrapper

@log_transaction
def transfer(amount):
    return amount

print(transfer(500))
