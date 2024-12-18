#if
age = 18
if age >= 18:
    print("You are an adult.")

#if with Logical Operators
num = 7
if num > 0 and num < 10:
    print("The number is a single-digit positive number.")


#if-else
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


'''Example Output:
You are an adult.
The number is a single-digit positive number.
You are a minor.
'''

#if-elif-else
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")

#Nested if Statement

num = 10
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is negative.")

'''Example Output:
Grade: B
The number is positive and even.
'''

#Using Conditional Statements with in or is
# Membership
fruit = "apple"
if fruit in ["apple", "banana", "cherry"]:
    print("Fruit is available.")

# Identity
x = None
if x is None:
    print("x has no value.")

'''Example Output:
Fruit is available.
x has no value.
'''

#break Statement

# Example: Stop the loop when a number is found
numbers = [1, 3, 5, 7, 9]
for num in numbers:
    if num == 5:
        print("Found 5! Exiting loop.")
        break
    print(num)

'''Example Output:
1
3
Found 5! Exiting loop.
'''

#Continue Statement

# Example: Skip even numbers
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)

'''Example Output:
1
3
5
7
9
'''

#pass Statement
# Example: Placeholder for future code
for i in range(5):
    if i == 2:
        pass  
    else:
        print(i)

'''Example Output:
0
1
3
4
'''
