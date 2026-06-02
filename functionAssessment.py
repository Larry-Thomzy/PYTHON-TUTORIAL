# Exercise 1: Student Course Registration System
#
# Create a program that:
#
# Stores available courses in a dictionary where:
# Key = course code
# Value = course name --

# Allows students to register courses.
# Prevents duplicate course registrations using a set.
# Uses a while loop to keep displaying a menu. --
# Uses a match statement for menu navigation.
# Stores registered courses in a list.
# Displays all registered courses using a for loop.
# Stores student information in a tuple (student_id, name).

course = {
    "web101" : "Web Development",
    "cyber404": "Cyber-Security",
    "dat213" : "Data-Analyst"
}
course_keys = list(course.keys())
reg_course = set()


def display_course():
    print("\n\nAvailable Courses: ")
    for i in course:
        print(i,":",course[i])
    print()
    print()


def register_course():
    count = 0
    print("\n\nCourse Registration")
    for i in course:
        count +=1
        print(count,".",i,":",course[i])
    option = int(input("Select a course to Register:"))
    if course_keys[option - 1] in reg_course:
        print("Course Already exists")
    else:
        match option:
            case 1: reg_course.add(course_keys[0])
            case 2: reg_course.add(course_keys[1])
            case 3: reg_course.add(course_keys[2])
        print("Course Registered Successfully\n\n\n")


def display_reg_course():
    print("\n\n===============Registered Courses================")
    for i in reg_course:
        print(i, ":", course[i])
    print("==================================================\n\n\n")





while True:
    print("==========Student Course Registration==========")
    print("      ===============Menu===============")
    print("1. Display Available courses")
    print("2. Register course")
    print("3. Display Registered Courses")
    print("4. Exit")

    opt = int(input("Select Option:"))
    if opt == 4:
        print("Exiting....")

    match opt:
        case 1: display_course()
        case 2: register_course()
        case 3: display_reg_course()
        case 4: break





#===================================================

# Exercise 2: Hospital Patient Queue Management
#
# Create a hospital system that:
#
# Stores patient records in a dictionary.
# Uses a list as a waiting queue.
# Prevents duplicate patient IDs using a set.
# Stores patient details as tuples.
# Uses a while loop for continuous operation.
# Uses a match statement for:
# Add patient
# Attend patient
# View queue
# Exit
# Uses a for loop to display all waiting patients.

#===================================================

# Exercise 3: Supermarket Inventory and Sales System
#
# Build a supermarket application that:
#
# Stores products and prices in a dictionary.
# Uses a list for purchased items.
# Uses a set to track unique customers.
# Stores product information as tuples.
# Uses a while loop for checkout operations.
# Uses a match statement for menu selection.
# Uses conditionals to verify stock availability.
# Uses a for loop to calculate total sales.

#===================================================


# Exercise 4: Online Voting System
#
# Develop a voting application that:
#
# Stores candidates in a dictionary.
# Uses a set to prevent duplicate voters.
# Stores voter information in tuples.
# Uses a while loop to continue voting.
# Uses a match statement for voting options.
# Uses conditionals to validate voters.
# Uses a for loop to display election results.

#===================================================

# Exercise 5: Bank Account Management System
#
# Create a banking application that:
#
# Stores account details in a dictionary.
# Stores customer details as tuples.
# Uses a while loop for ATM operations.
# Uses a match statement for:
# Deposit
# Withdraw
# Balance Inquiry
# Exit
# Uses conditionals to prevent overdrafts.
# Uses a list to maintain transaction history.
# Uses a for loop to display transactions.
# Uses a set to track unique account holders.

#===================================================

# Exercise 6: Event Ticket Booking System
#
# Build a ticket booking platform that:
#
# Stores events and available seats in a dictionary.
# Uses a set to prevent duplicate ticket bookings.
# Uses tuples for ticket information.
# Uses a list for booking records.
# Uses a while loop for menu navigation.
# Uses a match statement for:
# Book Ticket
# Cancel Ticket
# View Bookings
# Uses conditionals to verify seat availability.
# Uses a for loop to display all bookings.

#===================================================

# Exercise 7: School Result Processing System
#
# Create a result processing application that:
#
# Stores student scores in a dictionary.
# Stores student information in tuples.
# Uses a list to store subjects.
# Uses a set to track unique students.
# Uses a while loop for data entry.
# Uses a match statement for menu choices.
# Uses conditionals to assign grades.
# Uses a for loop to calculate averages and display results.

#===================================================


# Exercise 8: Hotel Reservation System
#
# Develop a hotel reservation application that:
#
# Stores room details in a dictionary.
# Uses a set to prevent duplicate bookings.
# Uses tuples for guest information.
# Uses a list for reservation history.
# Uses a while loop for operations.
# Uses a match statement for:
# Book Room
# Check Out
# View Reservations
# Uses conditionals to check room availability.
# Uses a for loop to display reservations.

#===================================================

# Exercise 9: Employee Attendance Tracker
#
# Build an attendance system that:
#
# Stores employee records in a dictionary.
# Uses a set to prevent duplicate attendance entries.
# Uses tuples for employee information.
# Uses a list for daily attendance logs.
# Uses a while loop for attendance marking.
# Uses a match statement for menu navigation.
# Uses conditionals to validate employee IDs.
# Uses a for loop to generate attendance reports.

#===================================================


# Exercise 10: Ride-Hailing Application
#
# Create a ride-booking system that:
#
# Stores drivers and their availability in a dictionary.
# Uses a set to prevent duplicate ride requests.
# Stores ride details as tuples.
# Uses a list to maintain ride history.
# Uses a while loop for continuous booking.
# Uses a match statement for:
# Request Ride
# Cancel Ride
# View Ride History
# Uses conditionals to determine driver availability.
# Uses a for loop to display all completed rides.