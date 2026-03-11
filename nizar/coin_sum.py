def coin_sum(amount: int, coins: list[int]) -> int:
    def count_ways(remaining, index):
        if remaining == 0:
            return 1
        elif remaining < 0 or index == len(coins):
            return 0
        else:
            return count_ways(remaining - coins[index], index) + count_ways(remaining, index + 1)
    return count_ways(amount, 0)


if __name__ == "__main__":
    print(coin_sum(5, [1, 2, 5]))    # 4 (ways: 5, 2+2+1, 2+1+1+1, 1+1+1+1+1)
    print(coin_sum(3, [2]))          # 0 (no way to make 3 with only 2s)
    print(coin_sum(0, [1, 2]))       # 1 (one way: use no coins)
    print(coin_sum(10, [1, 5, 10]))  # 4