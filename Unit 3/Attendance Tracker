#Mini Project – Attendance Tracker 
attendance = {}

while True:

    print("\n--- ATTENDANCE TRACKER ---")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. Display Attendance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        attendance[name] = []
        print("Student added successfully!")

    elif choice == 2:
        name = input("Enter student name: ")

        if name in attendance:
            status = input("Enter P for Present or A for Absent: ")

            if status.upper() in ["P", "A"]:
                attendance[name].append(status.upper())
                print("Attendance marked!")
            else:
                print("Invalid status!")

        else:
            print("Student not found!")

    elif choice == 3:
        print("\n--- Attendance Report ---")

        for name, records in attendance.items():
            present = records.count("P")
            absent = records.count("A")

            print("\nName:", name)
            print("Present:", present)
            print("Absent:", absent)
            print("Total Classes:", len(records))

            if len(records) > 0:
                percentage = (present / len(records)) * 100
                print("Attendance Percentage:", percentage, "%")

    elif choice == 4:
        break

    else:
        print("Invalid choice!")