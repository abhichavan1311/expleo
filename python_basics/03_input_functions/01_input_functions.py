#Basic Input Example
name = input("Enter your name: ")
print(f"Hello, {name}!")

#Input with Type Conversion
age = int(input("Enter your age: "))
print(f"You are {age} years old.")

# Input with Default Value
name = input("Enter your name (default: John): ").strip() or "John"
print(f"Hello, {name}!")


'''Example output:
Enter your name: abhi
Hello, abhi!
Enter your age: 30
You are 30 years old.
Enter your name (default: John):
Hello, John!
'''