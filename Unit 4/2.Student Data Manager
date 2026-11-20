#  Lab Exercise 2:Student Data Manager

while True:

    print("\n--- STUDENT DATA MANAGER ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        marks = input("Enter Marks: ")

        with open("students.txt", "a") as file:
            file.write(name + "," + roll + "," + marks + "\n")

        print("Student Added Successfully!")

    elif choice == "2":

        try:
            with open("students.txt", "r") as file:
                print("\nStudent Records:")
                print(file.read())

        except FileNotFoundError:
            print("No Student Records Found!")

    elif choice == "3":

        search = input("Enter Roll Number: ")
        found = False

        try:
            with open("students.txt", "r") as file:

                for line in file:
                    data = line.strip().split(",")

                    if len(data) == 3 and data[1] == search:
                        print("Name:", data[0])
                        print("Roll:", data[1])
                        print("Marks:", data[2])
                        found = True
                        break

            if not found:
                print("Student Not Found!")

        except FileNotFoundError:
            print("File Not Found!")

    elif choice == "4":
        print("Program Ended")
        break

    else:
        print("Invalid Choice!")