# Dictionary Example
student = {"name": "Alice", "age": 25, "grade": "A"}
print(f"Original Dictionary: {student}")
print(f"Name: {student['name']}")
student["age"] = 26
print(f"Updated Age: {student}")
student["city"] = "New York"
print(f"After Adding City: {student}")
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")

'''Example output:
PS D:\Before sunfire\Technocirrus\Technocirrus\training\expleo> & "C:/Users/Abhishek Chavan/AppData/Local/Microsoft/WindowsApps/python3.11.exe" "d:/Before sunfire/Technocirrus/Technocirrus/training/expleo/python_basics/01Standard_Data_type/06_Dictionary.py"
Original Dictionary: {'name': 'Alice', 'age': 25, 'grade': 'A'}
Name: Alice
Updated Age: {'name': 'Alice', 'age': 26, 'grade': 'A'}
After Adding City: {'name': 'Alice', 'age': 26, 'grade': 'A', 'city': 'New York'}   
Keys: ['name', 'age', 'grade', 'city']
Values: ['Alice', 26, 'A', 'New York']
PS D:\Before sunfire\Technocirrus\Technocirrus\training\expleo>
'''