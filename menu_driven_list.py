my_list = []

while True:
    print("\nMenu:")
    print("1. Create a new list")
    print("2. Add an element")
    print("3. Modify an element by index")
    print("4. Delete an element by index")
    print("5. Delete an element by value")
    print("6. Show the list")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        my_list = input("Enter elements separated by spaces: ").split()
        print("List created:", my_list)

    elif choice == "2":
        elem = input("Enter element to add: ")
        my_list.append(elem)
        print("Element added.")

    elif choice == "3":
        try:
            idx = int(input("Enter index to modify: "))
            new_val = input("Enter new value: ")
            my_list[idx] = new_val
            print("Element modified.")
        except (IndexError, ValueError):
            print("Invalid index.")

    elif choice == "4":
        try:
            idx = int(input("Enter index to delete: "))
            removed = my_list.pop(idx)
            print("Removed element:", removed)
        except (IndexError, ValueError):
            print("Invalid index.")

    elif choice == "5":
        val = input("Enter value to delete: ")
        if val in my_list:
            my_list.remove(val)
            print("Element removed.")
        else:
            print("Value not found in the list.")

    elif choice == "6":
        print("Current List:", my_list)

    elif choice == "7":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
