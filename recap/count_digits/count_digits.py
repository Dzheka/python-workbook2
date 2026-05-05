def count_digits(n: int) -> int:
    cnt = 0
    if n==0:
        return 1
    else:
        while n!=0:
            n=int(n/10)
            cnt+=1
    return cnt


if __name__ == "__main__":
    print(count_digits(0))  # 1
    print(count_digits(5))  # 1
    print(count_digits(123))  # 3
    print(count_digits(1000000))  # 7
