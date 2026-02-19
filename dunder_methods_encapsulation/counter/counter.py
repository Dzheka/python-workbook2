class Counter:
    def __init__(self, value = 0):
        self.value = value

    def increment(self):
        self.value += 1

    def __add__(self, other):
        counter = self.value + other.value
        return f"Counter({counter})"

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return f"Counter({self.value})"

    def __bool__(self):
        if self.value == 0:
            return False
        return  True



c1 = Counter()
c1.increment()
c1.increment()
c1.increment()
print(c1)           # Counter(3)

c2 = Counter(7)
c3 = c1 + c2
print(c3)           # Counter(10)
print(c1 == Counter(3))  # True

empty = Counter()
if not empty:
    print("Counter is zero!")  # This prints