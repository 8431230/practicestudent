def student_details(name, roll_no, course, marks):
    result = (
        f"Student Name: {name}\n"
        f"Roll No: {roll_no}\n"
        f"Course: {course}\n"
        f"Marks: {marks}"
    )
    return result


if __name__ == "__main__":
    name = "Amit"
    roll_no = "S101"
    course = "Computer Science"
    marks = 85

    print(student_details(name, roll_no, course, marks))
