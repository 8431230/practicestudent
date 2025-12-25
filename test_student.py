from student import student_details


def test_student_details():
    result = student_details("Amit", "S101", "Computer Science", 85)

    assert "Student Name: Amit" in result
    assert "Roll No: S101" in result
    assert "Course: Computer Science" in result
    assert "Marks: 85" in result
