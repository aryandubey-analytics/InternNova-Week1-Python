students = []

print("------ Student Record Management System ------")

while True:
    print("\n1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Name")
    print("4. Delete Student Record")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter student name: ").strip().title()
        age = int(input("Enter student age: "))
        course = input("Enter student course: ").strip().upper()

        student = {
            "Name": name,
            "Age": age,
            "Course": course
        }

        students.append(student)

        print("Student record added successfully.")

    elif choice == "2":
        print("\n------ All Student Records ------")

        if len(students) == 0:
            print("No student records found.")
        else:
            for student in students:
                print("Name:", student["Name"])
                print("Age:", student["Age"])
                print("Course:", student["Course"])
                print("--------------------")

    elif choice == "3":
        search_name = input("Enter student name to search: ").strip().title()

        found = False

        for student in students:
            if student["Name"] == search_name:
                print("\nStudent Found:")
                print("Name:", student["Name"])
                print("Age:", student["Age"])
                print("Course:", student["Course"])

                found = True
                break

        if not found:
            print("Student record not found.")

    elif choice == "4":
        delete_name = input("Enter student name to delete: ").strip().title()

        found = False

        for student in students:
            if student["Name"] == delete_name:
                students.remove(student)

                print("Student record deleted successfully.")

                found = True
                break

        if not found:
            print("Student record not found.")

    elif choice == "5":
        print("Exiting Student Record Management System...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")