class Student:
    def __init__(self,student_id,full_name,age,email,department):
        self.student_id = student_id
        self.full_name = full_name
        self.age = age
        self.email = email
        self.department = department
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)

    def display(self):
        print(f"{self.full_name} - {self.department}")

class Teacher:
    def __init__(self,name):
        self.name = name
        self.courses = []

    def assign_course(self,course):
        self.courses.append(course)

class Course:
    def __init__(self,code,title,unit):
        self.code = code
        self.title = title
        self.unit = unit

students = []
courses = []

# Register Student
def register_student():
    student_id = input("Enter ID: ")
    fullname = input("Enter fullname: ")
    age = int(input("Enter age: "))
    email = input("Enter email: ")
    department = input("Enter department: ")
    for student in students:
        if student.email == email:
            print("Duplicate email detected")
            return

    new_student = Student(student_id, fullname, age, email, department)
    students.append(new_student)

    with open("students.txt", "a") as file:
        file.write(f"{student_id},{fullname},{age},{email},{department}\n")
    print("Student registered successfully")


# register_student()


# DISPLAY STUDENT
# def display_students():
#     for student in students:
#         print(f"Student ID: {student.student_id}")

def search_student():
    search_term = input("Enter student ID or email to search: ").strip().lower()
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                # Remove trailing newline and split by comma
                parts = line.strip().split(",")
                if len(parts) >= 5:
                    student_id, fullname, age, email, department = parts[0], parts[1], parts[2], parts[3], parts[4]

                    # Check if search term matches ID or email
                    if search_term in student_id.lower() or search_term in email.lower():
                        print("\n--- Student Found ---")
                        print(f"ID: {student_id}")
                        print(f"Name: {fullname}")
                        print(f"Age: {age}")
                        print(f"Email: {email}")
                        print(f"Department: {department}")
                        found = True

        if not found:
            print("No matching student records found.")

    except FileNotFoundError:
        print("No student records file found yet. Register a student first.")

search_student()

# Register Courses

def register_courses():
    code = input("Enter course code: ")
    title = input("Enter course title: ")
    unit = int(input("Enter the credit unit number"))
    for course in courses:
        if course.code == code:
            print("Course already exists")
            return

    new_course = Course(code,title,unit)
    courses.append(new_course)

    with open("courses.txt", "a") as file:
        file.write(f"{code}, {title}, {unit}\n")
    print("Course registeres successfully")

# register_courses






#

# SQL EXAMPLES
# CREATE TABLE STUDENTS(
#  student_id int primary key,
#  full_name varchar(50),
#  age int,
#  email varchar(20),
#  department varchar (30),
#  );

 # INSERT INTO TABLE STUDENTS (full_name, age, email, department)
 # values ("Larry Thomzy", 22, "larrythomzy@gmail.com", "Science & Technology")