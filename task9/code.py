
# COMPREHENSIVE SMART CAMPUS MANAGEMENT SYSTEM

# Student records:
# [Student ID, Name, Department]

students = []

# Attendance:
# [Student ID, Present Days, Total Days]

attendance = []

# Marks:
# [Student ID, [Subject Marks]]

marks = []

# Event registrations:
# (Student ID, Event Name)

event_registrations = []

# Resource allocations:
# (Student ID, Resource Name)

resource_allocations = []

# Available campus events (tuple)
events = (
    "Technical Fest",
    "Sports Day",
    "Cultural Fest",
    "Science Exhibition"
)

# Available campus resources (tuple)
resources = (
    "Computer Lab",
    "Seminar Hall",
    "Sports Ground",
    "Library"
)


# Check whether student exists
def student_exists(sid):
    for student in students:
        if student[0] == sid:
            return True
    return False


# 1. STUDENT RECORD MANAGEMENT
def student_management():

    print("\n--- STUDENT MANAGEMENT ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")

    choice = input("Enter choice: ")

    if choice == "1":

        sid = input("Enter Student ID: ")

        if student_exists(sid):
            print("Student ID already exists!")
            return

        name = input("Enter Student Name: ")
        dept = input("Enter Department: ")

        student = [sid, name, dept]
        students.append(student)

        print("Student added successfully!")

    elif choice == "2":

        print("\nStudent Records:")

        if not students:
            print("No student records available.")

        for sid, name, dept in students:
            print("ID:", sid,
                  "Name:", name,
                  "Department:", dept)

    elif choice == "3":

        sid = input("Enter Student ID to search: ")

        found = False

        for student in students:

            if student[0] == sid:

                print("Student Found!")
                print("ID:", student[0])
                print("Name:", student[1])
                print("Department:", student[2])

                found = True
                break

        if not found:
            print("Student not found.")

    else:
        print("Invalid choice!")


# 2. ATTENDANCE MANAGEMENT
def attendance_management():

    print("\n--- ATTENDANCE MANAGEMENT ---")

    sid = input("Enter Student ID: ")

    if not student_exists(sid):
        print("Student not found!")
        return

    try:
        present = int(input("Enter Present Days: "))
        total = int(input("Enter Total Working Days: "))

        if total <= 0 or present < 0 or present > total:
            print("Invalid attendance details!")
            return

    except ValueError:
        print("Enter valid numeric values!")
        return

    # Update existing attendance or insert new record
    for record in attendance:

        if record[0] == sid:
            record[1] = present
            record[2] = total
            print("Attendance updated!")
            return

    attendance.append([sid, present, total])

    percentage = (present / total) * 100

    print("Attendance Recorded!")
    print("Attendance Percentage:",
          round(percentage, 2), "%")


# 3. MARKS MANAGEMENT
def marks_management():

    print("\n--- MARKS MANAGEMENT ---")

    sid = input("Enter Student ID: ")

    if not student_exists(sid):
        print("Student not found!")
        return

    try:
        n = int(input("Enter Number of Subjects: "))

        if n <= 0:
            print("Number of subjects must be positive!")
            return

        subject_marks = []

        for i in range(n):

            mark = float(
                input(f"Enter marks for Subject {i+1}: ")
            )

            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100!")
                return

            subject_marks.append(mark)

    except ValueError:
        print("Invalid numeric input!")
        return

    # Update existing marks
    for record in marks:

        if record[0] == sid:
            record[1] = subject_marks
            break

    else:
        marks.append([sid, subject_marks])

    total_marks = sum(subject_marks)
    average = total_marks / len(subject_marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    print("Total Marks:", total_marks)
    print("Average:", round(average, 2))
    print("Grade:", grade)


# 4. EVENT REGISTRATION
def event_management():

    print("\n--- EVENT REGISTRATION ---")

    sid = input("Enter Student ID: ")

    if not student_exists(sid):
        print("Student not found!")
        return

    print("Available Events:")

    for i, event in enumerate(events, start=1):
        print(i, ".", event)

    event_name = input("Enter Event Name: ")

    if event_name not in events:
        print("Invalid event!")
        return

    registration = (sid, event_name)

    if registration in event_registrations:
        print("Already registered!")
        return

    event_registrations.append(registration)

    print("Event Registration Successful!")


# 5. RESOURCE ALLOCATION
def resource_management():

    print("\n--- RESOURCE ALLOCATION ---")

    sid = input("Enter Student ID: ")

    if not student_exists(sid):
        print("Student not found!")
        return

    print("Available Resources:")

    for i, resource in enumerate(resources, start=1):
        print(i, ".", resource)

    resource_name = input("Enter Resource Name: ")

    if resource_name not in resources:
        print("Invalid resource!")
        return

    # One active allocation per student
    for allocation in resource_allocations:

        if allocation[0] == sid:
            print("Student already has an allocation!")
            return

    # Check resource availability
    allocated_names = [
        allocation[1]
        for allocation in resource_allocations
    ]

    if resource_name in allocated_names:
        print("Resource is currently allocated!")
        return

    # Store allocation as tuple
    allocation = (sid, resource_name)

    resource_allocations.append(allocation)

    print("Resource Allocated Successfully!")


# 6. SUMMARY REPORT
def summary_report():

    print("\n========== SMART CAMPUS SUMMARY ==========")

    if not students:
        print("No student records available.")
        return

    for sid, name, dept in students:

        print("\nStudent ID:", sid)
        print("Name:", name)
        print("Department:", dept)

        # Attendance report
        attendance_found = False

        for record in attendance:

            if record[0] == sid:

                present, total = record[1], record[2]

                percentage = (present / total) * 100

                print("Attendance:",
                      round(percentage, 2), "%")

                attendance_found = True
                break

        if not attendance_found:
            print("Attendance: Not recorded")

        # Marks report
        marks_found = False

        for mark_record in marks:

            if mark_record[0] == sid:

                subject_marks = mark_record[1]

                average = sum(subject_marks) / len(subject_marks)

                print("Subject Marks:", subject_marks)
                print("Average Marks:", round(average, 2))

                marks_found = True
                break

        if not marks_found:
            print("Marks: Not recorded")

        # Event report using tuple unpacking
        registered = [
            event
            for student_id, event in event_registrations
            if student_id == sid
        ]

        print("Registered Events:",
              registered if registered else "None")

        # Resource report using tuple unpacking
        allocated = [
            resource
            for student_id, resource in resource_allocations
            if student_id == sid
        ]

        print("Allocated Resources:",
              allocated if allocated else "None")

    print("\n========== CAMPUS STATISTICS ==========")

    print("Total Students:", len(students))
    print("Attendance Records:", len(attendance))
    print("Marks Records:", len(marks))
    print("Event Registrations:", len(event_registrations))
    print("Resource Allocations:", len(resource_allocations))


# MAIN MENU
while True:

    print("\n===================================")
    print("   SMART CAMPUS MANAGEMENT SYSTEM")
    print("===================================")

    print("1. Student Records")
    print("2. Attendance Management")
    print("3. Marks Management")
    print("4. Event Registration")
    print("5. Resource Allocation")
    print("6. Summary Report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_management()

    elif choice == "2":
        attendance_management()

    elif choice == "3":
        marks_management()

    elif choice == "4":
        event_management()

    elif choice == "5":
        resource_management()

    elif choice == "6":
        summary_report()

    elif choice == "7":
        print("Thank you for using Smart Campus System!")
        break

    else:
        print("Invalid menu choice! Try again.")


