# Adding Integer and Float
integer_value = 10
float_value = 3.5

result = integer_value + float_value
print(f"Sum of Integer and Float: {result}")
print(f"Product of Integer and Float: {integer_value * float_value}")

'''Example Output:
Sum of Integer and Float: 13.5
Product of Integer and Float: 35.0
PS D:\Before sunfire\Technocirrus\Technocirrus\training\expleo> 
'''

# String concatenation with List elements
greeting = "Hello"
names = ["Alice", "Bob", "Charlie"]

# Concatenating the greeting with each name
for name in names:
    print(f"{greeting}, {name}!")

# Add a string element to a list
names.append("David")
print(f"Updated Names List: {names}")

'''Example Output:
Hello, Alice!
Hello, Bob!
Hello, Charlie!
Updated Names List: ['Alice', 'Bob', 'Charlie', 'David']
'''
# Tuple and Set operations
coordinates = (10, 20, 30)
unique_numbers = {10, 20, 40}

# Combining tuple and set to find common values
common_values = set(coordinates) & unique_numbers
print(f"Common Values between Tuple and Set: {common_values}")

'''Example Output:
Common Values between Tuple and Set: {10, 20}
'''

# Dictionary with List Values
student_courses = {
    "Alice": ["Math", "Science"],
    "Bob": ["English", "History"],
    "Charlie": ["Math", "Art"]
}

# Accessing courses for a student
print(f"Alice's Courses: {student_courses['Alice']}")

# Adding a course for Bob
student_courses["Bob"].append("Physical Education")
print(f"Updated Courses for Bob: {student_courses['Bob']}")

'''
Example output: Alice's Courses: ['Math', 'Science']
Updated Courses for Bob: ['English', 'History', 'Physical Education']
'''

# Combined List
combined_list = [
    "Hello, World!",              # String
    [1, 2, 3],                    # List
    (10, 20),                     # Tuple
    42                            # Integer
]

print(f"Combined List: {combined_list}")

# Accessing Elements
print(f"First Element (String): {combined_list[0]}")
print(f"Second Element (List): {combined_list[1]}")
print(f"Third Element (Tuple): {combined_list[2]}")
print(f"Fourth Element (Integer): {combined_list[3]}")

'''Example Output:
Combined List: ['Hello, World!', [1, 2, 3], (10, 20), 42]
First Element (String): Hello, World!
Second Element (List): [1, 2, 3]
Third Element (Tuple): (10, 20)
Fourth Element (Integer): 42
'''