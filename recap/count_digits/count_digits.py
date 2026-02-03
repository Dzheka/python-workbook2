def count_digits(n: int) -> int:
    if n >= 0 and n <= 9:
        return 1
    elif n >= 10:
        return 1 + count_digits(n//10)
    else: 
        return count_digits(abs(n))


if __name__ == "__main__":
    print(count_digits(-125))  # 1
    print(count_digits(0))  # 1
    print(count_digits(123))  # 3
    print(count_digits(1000000))  # 7
