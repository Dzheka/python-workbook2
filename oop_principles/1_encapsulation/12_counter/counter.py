class Counter:
    def __init__(self,min_value = 0, max_value = 100):
        if min_value > max_value:
            raise ValueError("min_value must be less than max_value")
        self.min_value = min_value
        self.max_value = max_value
        self._count = min_value

    def increment(self,step):
        new_value = self._count + step
        if new_value > self.max_value:
            self._count = self.max_value
        else:
            self._count = new_value

    def decrement(self,step):
        new_value = self._count - step
        if new_value < self.min_value:
            self._count = self.min_value
        else:
            self._count = new_value

    def reset(self):
        self._count = self.min_value

    def get_value(self):
        return self._count

    def get_is_at_min(self):
        return self._count == self.min_value

    def get_is_at_max(self):
        return self._count == self.max_value

    def __str__(self):
        return f"Counter: {self._count}/{self.max_value} ({self.min_value}-{self.max_value})"



# Create counter with default bounds (0-100)
counter = Counter()
print(counter)              # "Counter: 0/100 (0-100)"
print(counter.get_value())        # 0
print(counter.get_is_at_min())    # True
print(counter.get_is_at_max())    # False

# Increment operations
counter.increment(1)                # +1
print(counter.get_value())         # 1
counter.increment(5)               # +5
print(counter.get_value())         # 6

# Decrement operations
counter.decrement(1)                # -1
print(counter.get_value())         # 5
counter.decrement(3)               # -3
print(counter.get_value())         # 2

# Reset counter
counter.reset()
print(counter.get_value())         # 0

# Custom bounds
game_counter = Counter(min_value=1, max_value=10)
print(game_counter.get_value())    # 1
game_counter.increment(15)         # Should not exceed max
print(game_counter.get_value())    # 10 (capped at maximum)
print(game_counter.get_is_at_max()) # True

# Boundary testing
game_counter.decrement(20)         # Should not go below min
print(game_counter.get_value())    # 1 (capped at minimum)

# Invalid counter creation
try:
    bad_counter = Counter(min_value=10, max_value=5)
except ValueError as e:
    print(e)  # "min_value must be less than max_value"