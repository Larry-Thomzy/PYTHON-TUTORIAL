# ============================================================
#        SCHOOL MANAGEMENT SYSTEM
#        BEGINNER PYTHON PRACTICAL ASSESSMENT
# ============================================================


# ============================================================
# PART 1 - SYSTEM LOGIN
# ============================================================

registered_email = "admin@school.com"
registered_password = "Python123"


def login():
    print("========================================")
    print("       SCHOOL MANAGEMENT SYSTEM")
    print("              LOGIN")
    print("========================================")

    email = input("Enter email: ")
    password = input("Enter password: ")

    if email == registered_email and password == registered_password:
        print("\nAccess granted")
        print("Welcome to the Student Management System")
        return True
    else:
        print("\nAccess denied")
        print("Invalid email or password")
        return False


# ============================================================
# PART 2 - STUDENT DATABASE
# ============================================================

students = {
    "ST001": {
        "name": "David",
        "age": 18,
        "department": "Computer Science",
        "level": 100
    },

    "ST002": {
        "name": "Sarah",
        "age": 19,
        "department": "Accounting",
        "level": 200
    },

    "ST003": {
        "name": "Michael",
        "age": 20,
        "department": "Engineering",
        "level": 300
    },

    "ST004": {
        "name": "Grace",
        "age": 18,
        "department": "Mass Communication",
        "level": 100
    },

    "ST005": {
        "name": "Daniel",
        "age": 21,
        "department": "Computer Science",
        "level": 400
    }
}


# ============================================================
# PART 3 - DISPLAY ALL STUDENTS
# ============================================================

def display_students():

    print("\n========================================")
    print("             STUDENT LIST")
    print("========================================")

    for student_id in students:
        student = students[student_id]

        print("\nStudent ID:", student_id)
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Department:", student["department"])
        print("Level:", student["level"])


# ============================================================
# PART 4 - SEARCH STUDENT
# ============================================================

def search_student():

    student_id = input("\nEnter Student ID: ")

    if student_id in students:

        student = students[student_id]

        print("\nStudent Found")
        print("--------------------")
        print("Student ID:", student_id)
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Department:", student["department"])
        print("Level:", student["level"])

    else:
        print("\nStudent not found")


# ============================================================
# PART 5 - COURSE REGISTRATION
# ============================================================

courses = [
    "Python",
    "Database Systems",
    "Web Development",
    "Mathematics",
    "Computer Networks",
    "English"
]


def display_courses():

    print("\n========================================")
    print("           AVAILABLE COURSES")
    print("========================================")

    number = 1

    for course in courses:
        print(number, ".", course)
        number = number + 1


# ============================================================
# PART 6 - STUDENT COURSE REGISTRATION
# ============================================================

student_courses = [
    "Python",
    "Mathematics",
    "Database Systems"
]


def show_student_courses():

    print("\n========================================")
    print("          DAVID'S COURSES")
    print("========================================")

    for course in student_courses:
        print(course)


# ============================================================
# PART 7 - REMOVE DUPLICATE COURSES USING A SET
# ============================================================

duplicate_courses = [
    "Python",
    "Mathematics",
    "Python",
    "Database Systems",
    "Mathematics"
]


def show_unique_courses():

    unique_courses = set(duplicate_courses)

    print("\n========================================")
    print("           UNIQUE COURSES")
    print("========================================")

    for course in unique_courses:
        print(course)


# ============================================================
# PART 8 - STUDENT PERSONAL INFORMATION USING A TUPLE
# ============================================================

student_information = (
    "David",
    18,
    "Computer Science"
)


def display_student_info():

    print("\n========================================")
    print("        STUDENT INFORMATION")
    print("========================================")

    print("Name:", student_information[0])
    print("Age:", student_information[1])
    print("Department:", student_information[2])


# ============================================================
# PART 9 - STUDENT RESULTS
# ============================================================

student_results = {
    "Python": 85,
    "Mathematics": 72,
    "English": 42,
    "Database Systems": 90
}


def calculate_results():

    print("\n========================================")
    print("          STUDENT RESULTS")
    print("========================================")

    for subject in student_results:

        score = student_results[subject]

        if score >= 50:
            print(subject, ":", score, "- Pass")
        else:
            print(subject, ":", score, "- Fail")


# ============================================================
# PART 10 - GRADE CLASSIFICATION
# ============================================================

def calculate_grade(score):

    if score >= 70:
        return "A"

    elif score >= 60:
        return "B"

    elif score >= 50:
        return "C"

    elif score >= 40:
        return "D"

    else:
        return "F"


def display_grades():

    print("\n========================================")
    print("          STUDENT GRADES")
    print("========================================")

    for subject in student_results:

        score = student_results[subject]

        grade = calculate_grade(score)

        print(subject, ":", score, "- Grade", grade)


# ============================================================
# PART 11 - DEPARTMENT LIST
# ============================================================

departments = [
    "Computer Science",
    "Accounting",
    "Computer Science",
    "Engineering",
    "Mass Communication",
    "Computer Science"
]


def display_departments():

    unique_departments = set(departments)

    print("\n========================================")
    print("             DEPARTMENTS")
    print("========================================")

    for department in unique_departments:
        print(department)


# ============================================================
# PART 12 - STUDENT REPORT
# ============================================================

def generate_student_report():

    print("\n========================================")
    print("           STUDENT REPORT")
    print("========================================")

    student_id = "ST001"

    student = students[student_id]

    print("Student ID:", student_id)
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Department:", student["department"])
    print("Level:", student["level"])

    print("\nCourses:")

    for course in student_courses:
        print(course)

    print("\nResults:")

    for subject in student_results:

        score = student_results[subject]

        grade = calculate_grade(score)

        print(subject, ":", score, "- Grade", grade)

    print("========================================")


# ============================================================
# PART 13 - MAIN SYSTEM
# ============================================================

def main_menu():
    choice = 0
    while True:
        print("\n========================================")
        print("      SCHOOL MANAGEMENT SYSTEM")
        print("========================================")

        print("1. Display Students")
        print("2. Search Student")
        print("3. Display Courses")
        print("4. Show Student Courses")
        print("5. Show Unique Courses")
        print("6. Display Student Information")
        print("7. Calculate Results")
        print("8. Generate Student Report")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_students()

        elif choice == "2":
            search_student()

        elif choice == "3":
            display_courses()

        elif choice == "4":
            show_student_courses()

        elif choice == "5":
            show_unique_courses()

        elif choice == "6":
            display_student_info()

        elif choice == "7":
            calculate_results()

        elif choice == "8":
            generate_student_report()

        elif choice == "9":
            print("Exiting.......")
            break
        else:
            print("\nInvalid choice")


# ============================================================
# START PROGRAM
# ============================================================

login_successful = login()

if login_successful:
    main_menu()