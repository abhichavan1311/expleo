# Multiple Inputs on a Single Line
x, y = map(int, input("Enter two numbers separated by space: ").split())
print(f"The sum of {x} and {y} is {x + y}.")

#Input with Validation (Retry on Invalid Input)
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        break
    print("Invalid input. Please enter a valid number.")
print(f"Your age is {age}.")

#yes/No Input

confirm = input("Do you want to continue? (yes/no): ").strip().lower()
if confirm == "yes":
    print("Continuing...")
else:
    print("Exiting...")

#Input for a List
numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
print(f"You entered: {numbers}")

#Input with a Menu
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = int(input("Enter your choice (1-4): "))
if choice == 1:
    print("You chose addition.")
elif choice == 2:
    print("You chose subtraction.")
elif choice == 3:
    print("You chose multiplication.")
elif choice == 4:
    print("You chose division.")
else:
    print("Invalid choice.")

#Using get_user_input Pattern

def get_user_input(prompt, default_value):
    user_input = input(f"{prompt} (default: {default_value}): ")
    return user_input if user_input else default_value

name = get_user_input("Enter your name", "John")
age = int(get_user_input("Enter your age", 25))

print(f"Hello {name}, you are {age} years old.")


#Password Input (Masking Included)

import getpass

password = getpass.getpass("Enter your password: ")
if password == "admin123":
    print("Access granted.")
else:
    print("Access denied.")


'''Example Output:
Enter two numbers separated by space: 54 7
The sum of 54 and 7 is 61.
Enter your age: 30
Your age is 30.
Do you want to continue? (yes/no): no
Exiting...
Enter a list of numbers separated by space: 6 5 8 10 165 747637 6 8
You entered: [6, 5, 8, 10, 165, 747637, 6, 8]
1. Add
2. Subtract
3. Multiply
4. Divide
Enter your choice (1-4): 1
You chose addition.
Enter your name (default: John): kunal
Enter your age (default: 25): 29
Hello kunal, you are 29 years old.
Enter your password: 
Access denied.
'''