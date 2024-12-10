from abc import ABC, abstractmethod

class CollegeSystem(ABC):

    @abstractmethod
    def add_student(self):
        pass

    @abstractmethod
    def view_students(self):
        pass

    @abstractmethod
    def add_course(self):
        pass

    @abstractmethod
    def view_courses(self):
        pass

    @abstractmethod
    def enroll_student(self):
        pass

    @abstractmethod
    def view_enrollments(self):
        pass

class CollegeManagement(CollegeSystem):

    def __init__(self):
        self.students = {}
        self.courses = {}
        self.enrollments = {}

    def title(self):
        print("College Management System")

    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        if student_id in self.students:
            print("Student ID already exists.")
        else:
            self.students[student_id] = name
            print(f"Student '{name}' has been added.")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return
        print("\nList of Students:")
        for student_id, name in self.students.items():
            print(f"ID: {student_id}, Name: {name}")

    def add_course(self):
        course_code = input("Enter course code: ")
        course_name = input("Enter course name: ")
        if course_code in self.courses:
            print("Course code already exists.")
        else:
            self.courses[course_code] = course_name
            print(f"Course '{course_name}' has been added.")

    def view_courses(self):
        if not self.courses:
            print("No courses available.")
            return
        print("\nList of Courses:")
        for course_code, course_name in self.courses.items():
            print(f"Code: {course_code}, Name: {course_name}")

    def enroll_student(self):
        self.view_students()
        self.view_courses()
        student_id = input("Enter student ID to enroll: ")
        course_code = input("Enter course code to enroll in: ")
        if student_id in self.students and course_code in self.courses:
            self.enrollments.setdefault(student_id, []).append(course_code)
            print(f"Student '{self.students[student_id]}' has been enrolled in '{self.courses[course_code]}'.")
        else:
            print("Invalid student ID or course code.")

    def view_enrollments(self):
        if not self.enrollments:
            print("No enrollments available.")
            return
        print("\nEnrollments:")
        for student_id, course_codes in self.enrollments.items():
            student_name = self.students[student_id]
            print(f"Student: {student_name} (ID: {student_id}) - Courses: {', '.join(course_codes)}")

# Main Program
college = CollegeManagement()
college.title()

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Add Course")
    print("4. View Courses")
    print("5. Enroll Student")
    print("6. View Enrollments")
    print("7. Exit")

    choice = input("Please enter your choice: ")

    if choice == '1':
        college.add_student()
    elif choice == '2':
        college.view_students()
    elif choice == '3':
        college.add_course()
    elif choice == '4':
        college.view_courses()
    elif choice == '5':
        college.enroll_student()
    elif choice == '6':
        college.view_enrollments()
    elif choice == '7':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice, please try again.")
