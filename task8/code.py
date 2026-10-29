

students = []
attendance = []       
marks = []            
registrations = []  
allocations = []     

resources = [
    ["Computer Lab", 2],
    ["Library Book", 5],
    ["Sports Kit", 3]
]

while True:
    print("\n===== SMART CAMPUS MANAGEMENT =====")
    print("1. Add student")
    print("2. Record attendance")
    print("3. Enter examination marks")
    print("4. Register for event")
    print("5. Allocate resource")
    print("6. Summary report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sid = input("Enter student ID: ")
        exists = False

        for student_id, name, dept in students:
            if student_id == sid:
                exists = True

        if exists:
            print("Student ID already exists")
        else:
            name = input("Enter student name: ")
            dept = input("Enter department: ")
            students.append((sid, name, dept))
            print("Student added successfully")

    elif choice == "2":
        sid = input("Enter student ID: ")
        found = False

        for student_id, name, dept in students:
            if student_id == sid:
                found = True
                break

        if not found:
            print("Student not found")
        else:
            attended = int(input("Classes attended: "))
            total = int(input("Total classes: "))

            if total <= 0 or attended < 0 or attended > total:
                print("Invalid attendance details")
            else:
                updated = False

                for record in attendance:
                    if record[0] == sid:
                        record[1] = attended
                        record[2] = total
                        updated = True

                if not updated:
                    attendance.append([sid, attended, total])

                percentage = attended / total * 100
                print("Attendance:", round(percentage, 2), "%")

    elif choice == "3":
        sid = input("Enter student ID: ")
        found = False

        for student_id, name, dept in students:
            if student_id == sid:
                found = True
                break

        if not found:
            print("Student not found")
        else:
            scores = []
            valid = True

            for i in range(3):
                score = float(input(f"Enter mark {i + 1}: "))
                if score < 0 or score > 100:
                    valid = False
                scores.append(score)

            if not valid:
                print("Invalid marks. Enter values from 0 to 100.")
            else:
                updated = False

                for record in marks:
                    if record[0] == sid:
                        record[1] = scores
                        updated = True

                if not updated:
                    marks.append([sid, scores])

                print("Average marks:", round(sum(scores) / 3, 2))

    elif choice == "4":
        sid = input("Enter student ID: ")
        found = False

        for student_id, name, dept in students:
            if student_id == sid:
                found = True
                break

        if not found:
            print("Student not found")
        else:
            event = input("Enter event name: ")
            registration = (sid, event)

            if registration in registrations:
                print("Already registered")
            else:
                registrations.append(registration)
                print("Event registration successful")

    elif choice == "5":
        sid = input("Enter student ID: ")
        found = False

        for student_id, name, dept in students:
            if student_id == sid:
                found = True
                break

        if not found:
            print("Student not found")
        else:
            print("Available resources:")

            for resource in resources:
                used = 0

                for allocated_id, resource_name in allocations:
                    if resource_name == resource[0]:
                        used += 1

                available = resource[1] - used
                print(resource[0], "- Available:", available)

            requested = input("Enter resource name: ")
            matched = False

            for resource in resources:
                if resource[0].lower() == requested.lower():
                    matched = True
                    used = 0

                    for allocated_id, resource_name in allocations:
                        if resource_name == resource[0]:
                            used += 1

                    if used < resource[1]:
                        allocations.append((sid, resource[0]))
                        print("Resource allocated successfully")
                    else:
                        print("Resource not available")

            if not matched:
                print("Invalid resource name")

    elif choice == "6":
        print("\n===== CAMPUS SUMMARY REPORT =====")

        print("\nStudent Records:")
        for student_id, name, dept in students:
            print(student_id, name, dept)

        print("\nAttendance:")
        for sid, attended, total in attendance:
            print(sid, round(attended / total * 100, 2), "%")

        print("\nExamination Marks:")
        for sid, scores in marks:
            print(sid, scores, "Average:", round(sum(scores) / 3, 2))

        print("\nEvent Registrations:")
        for sid, event in registrations:
            print(sid, event)

        print("\nResource Allocations:")
        for sid, resource in allocations:
            print(sid, resource)

        print("\nAvailable Resources:")
        for resource in resources:
            used = 0

            for sid, resource_name in allocations:
                if resource_name == resource[0]:
                    used += 1

            print(resource[0], resource[1] - used, "available")

    elif choice == "7":
        print("Exiting Smart Campus Management System")
        break

    else:
        print("Invalid choice. Please try again.")

