import types
from student_report import student_report

STUDENTS = [
    {"name": "Alice", "grade": 95},
    {"name": "Bob",   "grade": 83},
    {"name": "Carol", "grade": 74},
    {"name": "Dan",   "grade": 55},
]

def test_returns_generator():
    result = student_report(STUDENTS)
    assert isinstance(result, types.GeneratorType)

def test_grade_a():
    result = list(student_report([{"name": "Alice", "grade": 95}]))
    assert result[0] == "Alice: A"

def test_grade_b():
    result = list(student_report([{"name": "Bob", "grade": 83}]))
    assert result[0] == "Bob: B"

def test_grade_f():
    result = list(student_report([{"name": "Dan", "grade": 55}]))
    assert result[0] == "Dan: F"

def test_full_list():
    result = list(student_report(STUDENTS))
    assert result == ["Alice: A", "Bob: B", "Carol: C", "Dan: F"]