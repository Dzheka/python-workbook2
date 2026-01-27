from student_grades import get_status, process_grades


def test_get_status_pass():
    assert get_status(50) == "Pass"
    assert get_status(85) == "Pass"
    assert get_status(100) == "Pass"


def test_get_status_fail():
    assert get_status(49) == "Fail"
    assert get_status(25) == "Fail"
    assert get_status(0) == "Fail"


def test_process_grades_basic():
    raw_scores = [
        ["Alice", 85],
        ["Bob", 42],
        ["Charlie", 60],
        ["David", 25],
        ["Eve", 95]
    ]
    result = process_grades(raw_scores)

    assert result == {
        "Alice": "Pass",
        "Bob": "Fail",
        "Charlie": "Pass",
        "David": "Fail",
        "Eve": "Pass"
    }


def test_process_grades_boundary():
    raw_scores = [
        ["John", 50],
        ["Jane", 49]
    ]
    result = process_grades(raw_scores)

    assert result == {
        "John": "Pass",
        "Jane": "Fail"
    }


def test_process_grades_empty():
    raw_scores = []
    result = process_grades(raw_scores)
    assert result == {}


def test_process_grades_all_pass():
    raw_scores = [
        ["Student1", 100],
        ["Student2", 90],
        ["Student3", 80]
    ]
    result = process_grades(raw_scores)

    assert result == {
        "Student1": "Pass",
        "Student2": "Pass",
        "Student3": "Pass"
    }


def test_process_grades_all_fail():
    raw_scores = [
        ["Student1", 30],
        ["Student2", 20],
        ["Student3", 10]
    ]
    result = process_grades(raw_scores)

    assert result == {
        "Student1": "Fail",
        "Student2": "Fail",
        "Student3": "Fail"
    }
