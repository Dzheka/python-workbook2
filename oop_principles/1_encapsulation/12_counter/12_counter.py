class Counter:


    def __init__(self, min_value=0, max_value=100):
        if min_value >= max_value:
            raise ValueError("min_value must be less than max_value")

        self.min_value = min_value
        self.max_value = max_value
        self._count    = min_value
        self.history   = []


    def get_value(self):
        return self._count


    def get_is_at_min(self):
        return self._count == self.min_value


    def get_is_at_max(self):
        return self._count == self.max_value


    def increment(self, step=1):
        self._count = self._count + step
        if self._count > self.max_value:
            self._count = self.max_value
        self.history.append(f"increment({step})")


    def decrement(self, step=1):
        self._count = self._count - step
        if self._count < self.min_value:
            self._count = self.min_value
        self.history.append(f"decrement({step})")


    def reset(self):
        self._count = self.min_value
        self.history.append("reset()")


    def __str__(self):
        return f"Counter: {self._count}/{self.max_value} ({self.min_value}-{self.max_value})"



counter = Counter()
print(counter)
print(counter.get_value())
print(counter.get_is_at_min())
print(counter.get_is_at_max())

counter.increment()
print(counter.get_value())
counter.increment(5)
print(counter.get_value())

counter.decrement()
print(counter.get_value())
counter.decrement(3)
print(counter.get_value())

counter.reset()
print(counter.get_value())


game_counter = Counter(min_value=1, max_value=10)
game_counter.increment(15)
print(game_counter.get_value())

game_counter.decrement(20)
print(game_counter.get_value())


try:
    bad_counter = Counter(min_value=10, max_value=5)
except ValueError as e:
    print(e)

