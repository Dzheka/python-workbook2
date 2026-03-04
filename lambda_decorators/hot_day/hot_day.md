**Topic:** Weather | **Concept:** Generator

Write:

1. A generator function `hot_days(temperatures)` — receives a list of `(day, temperature)` tuples and yields only days where temperature is **above 30°C**

2. A regular function `first_n_hot(temperatures, n)` — uses the generator and returns the first `n` hot days as a list

```python
# Your code here
```

**Expected output:**
```python
data = [("Mon", 28), ("Tue", 35), ("Wed", 31), ("Thu", 22), ("Fri", 33)]
list(hot_days(data))        # → [("Tue", 35), ("Wed", 31), ("Fri", 33)]
first_n_hot(data, 2)        # → [("Tue", 35), ("Wed", 31)]
```
