import json

# JSON-Based Log File Analyzer

logs = []

while True:

    print("\n--- LOG FILE ANALYZER ---")
    print("1. Add Log")
    print("2. Display Logs")
    print("3. Analyze Logs")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        username = input("Enter Username: ")
        status = input("Enter Status (success/failed): ")

        if status.lower() not in ["success", "failed"]:
            print("Invalid Status!")
            continue

        log = {
            "username": username,
            "status": status.lower()
        }

        logs.append(log)

        with open("logs.json", "w") as file:
            json.dump(logs, file, indent=4)

        print("Log Added Successfully!")

    elif choice == "2":

        try:
            with open("logs.json", "r") as file:
                data = json.load(file)

            print("\nLog Records:")
            for log in data:
                print(log)

        except FileNotFoundError:
            print("Log File Not Found!")

    elif choice == "3":

        try:
            with open("logs.json", "r") as file:
                data = json.load(file)

            success = 0
            failed = 0

            for log in data:

                if log["status"] == "success":
                    success += 1

                elif log["status"] == "failed":
                    failed += 1

            print("\n--- LOG ANALYSIS REPORT ---")
            print("Total Logs:", len(data))
            print("Successful Logs:", success)
            print("Failed Logs:", failed)

        except FileNotFoundError:
            print("Log File Not Found!")

    elif choice == "4":
        print("Program Ended")
        break

    else:
        print("Invalid Choice!")
