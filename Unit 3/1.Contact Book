# Lab Exercise 1:Contact Book using Lists and Dictionaries
contacts = []

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Display Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contact = {
            "name": name,
            "phone": phone
        }

        contacts.append(contact)
        print("Contact added successfully!")

    elif choice == 2:
        name = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["name"] == name:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                found = True

        if not found:
            print("Contact not found!")

    elif choice == 3:
        for contact in contacts:
            print(contact)

    elif choice == 4:
        name = input("Enter name to delete: ")

        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                print("Contact deleted!")
                break
        else:
            print("Contact not found!")

    elif choice == 5:
        break

    else:
        print("Invalid choice!")