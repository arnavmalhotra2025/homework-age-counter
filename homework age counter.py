def check_age():
    age_input = input("Enter your age: ")

    if not age_input.isdigit():
        raise ValueError("Invalid input. Please enter a whole number (integer) only.")

    age = int(age_input)

    if age % 2 == 0:
        print(f"Your age ({age}) is even.")
    else:
        print(f"Your age ({age}) is odd.")
