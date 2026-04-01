def log_transaction(func):
    def wrapper(*args, **kwargs):
        print("Transaction started")
        result = func(*args, **kwargs)
        print(f"Transaction finished: {result}")
        return result

    return wrapper


@log_transaction
def transfer(amount):
    return amount



print(transfer(50))
