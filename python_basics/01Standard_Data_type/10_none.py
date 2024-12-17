# None Example
result = None
print(f"Result: {result}")
if result is None:
    print("Result is not assigned yet.")

#actual_use
def greet(name=None):
    if name is None:
        print("Hello, Guest!")
    else:
        print(f"Hello, {name}!")

greet()        # Output: Hello, Guest!
greet("Alice") # Output: Hello, Alice!

'''Example Output:
Chavan/AppData/Local/Microsoft/WindowsApps/python3.11.exe" "d:/Before sunfire/Technocirrus/Technocirrus/training/expleo/python_basics/01Standard_Data_type/10_none.py"
Result: None
Result is not assigned yet.
PS D:\Before sunfire\Technocirrus\Technocirrus\training\expleo> & "C:/Users/Abhishek Chavan/AppData/Local/Microsoft/WindowsApps/python3.11.exe" "d:/Before sunfire/Technocirrus/Technocirrus/training/expleo/python_basics/01Standard_Data_type/10_none.py"
Result: None
Result is not assigned yet.
Hello, Guest!
Hello, Alice!
PS D:\Before sunfire\Technocirrus\Technocirrus\training\expleo>
'''
