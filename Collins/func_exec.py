# # Exercise 1: Student Course Registration System
# #
# # Create a program that:
# #
#
# #
# # Allows students to register courses.
# # Prevents duplicate course registrations using a set.
# # Uses a while loop to keep displaying a menu. --
# # Uses a match statement for menu navigation.
# # Stores registered courses in a list.
# # Displays all registered courses using a for loop.
# # Stores student information in a tuple (student_id, name).
# # 1
# # Stores available courses in a dictionary where:
# # Key = course code
# # Value = course name --
#
# course = {
#     "webdev201": "Web Development",
#     "basic500": "basic-Technology",
#     "datapro789": "Data-Processing"
# }fu
#
# course_keys = list(course.keys())
# reg_course = set()
#
#
# def display_course():
#     print("\n\nAvailable Courses: ")
#     for i in course:
#         print(i,":",course[i])
#     print()
#     print()
#

password = "larry"
result = []
for ch in password:
    result.append(ch.isupper())

print(result)
print(any(result))