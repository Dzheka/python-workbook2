import pytest
from classroom import Classroom

def test_add_and_average():
    c = Classroom()
    c.add_student("Alice", 90, 80, 100)
    assert c.average("Alice") == 90.0

def test_top_student():
    c = Classroom()
    c.add_student("Alice", 90, 85, 92)
    c.add_student("Bob", 70, 60, 80)
    assert c.top_student() == "Alice"

def test_remove_student():
    c = Classroom()
    c.add_student("Alice", 80)
    c.remove_student("Alice")
    assert "Alice" not in c.students

def test_remove_nonexistent_raises():
    c = Classroom()
    with pytest.raises(ValueError):
        c.remove_student("Ghost")

def test_multiple_students_top():
    c = Classroom()
    c.add_student("A", 100)
    c.add_student("B", 50)
    c.add_student("C", 75)
    assert c.top_student() == "A"