**Topic:** Students | **Concept:** OOP + Dicts

Write a class `Classroom` with:
- `__init__(self)` — empty dict of students
- `add_student(name, *grades)` — adds student with a list of grades
- `average(name)` — returns the average grade for that student (float)
- `top_student()` — returns the name of the student with the highest average
- `remove_student(name)` — removes student; raises `ValueError` if not found

```python
# Your code here
```

**Expected output:**
```python
c = Classroom()
c.add_student("Alice", 90, 85, 92)
c.add_student("Bob", 70, 60, 80)
c.average("Alice")    # → 89.0
c.top_student()       # → "Alice"
c.remove_student("Ghost")  # → ValueError
```

---