**Topic:** Weather | **Concept:** Decorator + Lambda

1. Write a decorator `celsius_only` that checks the first argument of a function. If it is below `-90` or above `60`, raise `ValueError("Invalid temperature")`. Otherwise call the function normally.

2. Write a lambda `classifier` that returns:
    - `"cold"` if temp < 10
    - `"warm"` if 10 <= temp < 25
    - `"hot"` if temp >= 25

3. Apply the decorator to `describe_weather(temp)` which calls `classifier` and returns the result.

```python
# Your code here
```

**Expected output:**
```python
describe_weather(30)    # → "hot"
describe_weather(-5)    # → "cold"
describe_weather(100)   # → ValueError: Invalid temperature
```
