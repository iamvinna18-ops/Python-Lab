# Lab Exercise 3:CSV-Based Payroll Management System
import csv

# Payroll Management System

while True:

    print("\n--- PAYROLL MANAGEMENT ---")
    print("1. Add Employee")
    print("2. Display Payroll")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter Employee Name: ")
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Basic Salary: "))
        bonus = float(input("Enter Bonus: "))

        total = salary + bonus

        with open("payroll.csv", "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([name, emp_id, salary, bonus, total])

        print("Employee Added Successfully!")

    elif choice == "2":

        try:
            with open("payroll.csv", "r") as file:
                reader = csv.reader(file)

                print("\nName | ID | Salary | Bonus | Total")

                for row in reader:
                    print(row)

        except FileNotFoundError:
            print("Payroll File Not Found!")

    elif choice == "3":
        print("Program Ended")
        break

    else:
        print("Invalid Choice!")