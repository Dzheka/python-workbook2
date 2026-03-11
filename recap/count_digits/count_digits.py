def count_digits(n: int) -> int:
    n = abs(n)

    if n == 0:
        return 1

    count = 0
    while n > 0:
        count += 1
        n //= 10

    return count


if __name__ == "__main__":
    print(count_digits(0))        # 1
    print(count_digits(5))        # 1
    print(count_digits(123))      # 3
    print(count_digits(1000000))  # 7
