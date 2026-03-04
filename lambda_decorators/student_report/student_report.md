**Topic:** Students | **Concept:** Generator

Write a **generator function** `student_report(students)` that receives a list of student dicts (with `"name"` and `"grade"`) and **yields** formatted strings one by one:

| Grade range | Letter |
|---|---|
| 90–100 | A |
| 80–89  | B |
| 70–79  | C |
| below 70 | F |

Do **not** build a list inside — use `yield`.

```python
# Your code here
```

**Expected output:**
```python
data = [{"name": "Alice", "grade": 95}, {"name": "Dan", "grade": 55}]
list(student_report(data))   # → ["Alice: A", "Dan: F"]
```

---