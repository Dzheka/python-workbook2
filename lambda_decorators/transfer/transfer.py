def log_transaction(func):
    def wrapper(*amount):
        print("Transaction started")
        result = func(*amount)
        print(f"Transaction finished: {amount[0]}")
        return result
    return wrapper


@log_transaction
def transfer(amount):
    return amount


transfer(500)
# Transaction started
# Transaction finished: 500
# → 500