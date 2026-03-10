class Counter:
    def __init__(self, min_value=0, max_value=100):
        if min_value >= max_value:
            raise ValueError("min_value must be less than max_value")
        self._min = min_value
        self._max = max_value
        self._count = min_value

    def get_value(self):
        return self._count

    def get_is_at_min(self):
        return self._count == self._min

    def get_is_at_max(self):
        return self._count == self._max

    def increment(self, step=1):
        self._count = min(self._count + step, self._max)

    def decrement(self, step=1):
        self._count = max(self._count - step, self._min)

    def reset(self):
        self._count = self._min

    def __str__(self):
        return f"Counter: {self._count}/{self._max} ({self._min}-{self._max})"
