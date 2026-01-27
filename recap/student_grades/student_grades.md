# Student Grades - Pass or Fail

Convert a list of student scores into a dictionary showing whether each student passed or failed.

## Input
A list of lists where each inner list contains:
- Student name (string)
- Score (integer)

## Tasks

### Part A: Status Logic Function
Create a function `get_status(score)`:
- If score >= 50, return "Pass"
- Otherwise, return "Fail"

### Part B: Grade Processor
Create a function `process_grades(data)`:
- Create an empty dictionary
- Loop through the data
- For each student, use `get_status()` to determine their status
- Add to dictionary: key = student name, value = status

## Examples

### Example 1
```python
raw_scores = [
    ["Alice", 85],
    ["Bob", 42],
    ["Charlie", 60],
    ["David", 25],
    ["Eve", 95]
]

result = process_grades(raw_scores)
print(result)
# {
#     "Alice": "Pass",
#     "Bob": "Fail",
#     "Charlie": "Pass",
#     "David": "Fail",
#     "Eve": "Pass"
# }
```

### Example 2
```python
raw_scores = [
    ["John", 50],
    ["Jane", 49]
]

result = process_grades(raw_scores)
print(result)
# {
#     "John": "Pass",
#     "Jane": "Fail"
# }
```

### Example 3
```python
raw_scores = []
result = process_grades(raw_scores)
print(result)  # {}
```
