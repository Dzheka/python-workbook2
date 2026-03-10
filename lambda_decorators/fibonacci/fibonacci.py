def fibonacci(n: int) -> int:
    def fib_generator():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    gen = fib_generator()
    for _ in range(n + 1):
        result = next(gen)
    return result


if __name__ == "__main__":
    print(fibonacci(0))   # 0
    print(fibonacci(1))   # 1
    print(fibonacci(6))   # 8
    print(fibonacci(10))  # 55
