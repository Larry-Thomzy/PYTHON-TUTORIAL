class Student:
    def __init__(self, student_id,fullname,age,email,department):
        self.student_id = student_id
        self.fullname = fullname
        self.age = age
        self.email = email
        self.department = department
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)

    def display(self):
        print(f"{self.fullname} -- {self.department} ")


class Teacher:
    def __int__(self, name):
        self.name = name
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)


class Course:
    def __int__(self, code, title, unit):
        self.code = code
        self.title = title
        self.unit = unit


students = []


def register_student():
    student_id = input("Enter ID: ")
    fullname = input("Enter full name: ")
    age = int(input("Enter age: "))
    email = input("Enter email: ")
    department = input("Enter department: ")

    for s in students:
        if s.email == email:
            print(f"{s.email} already exist")
            return
    new_student = Student(student_id, fullname, age, email, department)
    students.append(new_student)

    try:
        with open("C:/Users/LANRE//Desktop//studensts.txt", "a") as f:
            f.write(f"{fullname}, {email}, {department}\n")
    except:
        print("Registration failed")

    print("Student registered successfully")


register_student()
register_student()








