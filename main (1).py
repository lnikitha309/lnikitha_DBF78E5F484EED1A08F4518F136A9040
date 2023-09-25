class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa
def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students
if __name__ == "__main__":
    students1 = [
        Student("Alice", "A001", 3.8),
        Student("Bob", "B002", 3.5),
        Student("Charlie", "C003", 3.9),
        Student("David", "D004", 3.7),
    ]
    students2 = [
        Student("Eve", "E005", 3.6),
        Student("Frank", "F006", 3.2),
        Student("Grace", "G007", 3.9),
        Student("Hannah", "H008", 3.4),
    ]
    sorted_students1 = sort_students(students1)
    sorted_students2 = sort_students(students2)
    print("Sorted Students List 1 (Descending Order of CGPA):")
    for student in sorted_students1:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
    print("\nSorted Students List 2 (Descending Order of CGPA):")
    for student in sorted_students2:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
