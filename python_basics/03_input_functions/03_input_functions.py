
#Password Input (Masking not Included)

password = input("Enter your password: ")
if password == "admin123":
    print("Access granted.")
else:
    print("Access denied.")

'''Example Output:
Enter your password: Kunal@123
Access denied.
'''

#Perform Operations on a List of Numbers

# Get the list of numbers from the user
numbers = list(map(float, input("Enter a list of numbers separated by space: ").split()))
print(f"You entered: {numbers}")

# Display the menu
print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = int(input("Enter your choice (1-4): "))

if not numbers:
    print("Error: You must enter at least one number.")
elif choice == 1:
    # Add all numbers
    result = sum(numbers)
    print(f"The result of addition is: {result}")
elif choice == 2:
    # Subtract all numbers in sequence
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    print(f"The result of subtraction is: {result}")
elif choice == 3:
    # Multiply all numbers
    result = 1
    for num in numbers:
        result *= num
    print(f"The result of multiplication is: {result}")
elif choice == 4:
    # Divide all numbers in sequence
    result = numbers[0]
    try:
        for num in numbers[1:]:
            result /= num
        print(f"The result of division is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please enter a number between 1 and 4.")

'''Example output1:
Enter a list of numbers separated by space: 465 7566 78
You entered: [465.0, 7566.0, 78.0]

1. Add
2. Subtract
3. Multiply
4. Divide
Enter your choice (1-4): 3
The result of multiplication is: 274418820.0


Example Output2:
Enter a list of numbers separated by space:
You entered: []

1. Add
2. Subtract
3. Multiply
4. Divide
Enter your choice (1-4): 1
Error: You must enter at least one number.
'''