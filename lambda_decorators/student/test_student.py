from student import sort_by_grade, passing, get_names

STUDENTS = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob",   "grade": 72},
    {"name": "Carol", "grade": 95},
    {"name": "Dan",   "grade": 60},
]

def test_sort_by_grade_first():
    result = sort_by_grade(STUDENTS)
    assert result[0]["name"] == "Carol"

def test_sort_by_grade_last():
    result = sort_by_grade(STUDENTS)
    assert result[-1]["name"] == "Dan"

def test_passing_count():
    assert len(passing(STUDENTS)) == 3

def test_passing_excludes_failing():
    names = [s["name"] for s in passing(STUDENTS)]
    assert "Dan" not in names

def test_get_names():
    assert get_names(STUDENTS) == ["Alice", "Bob", "Carol", "Dan"]