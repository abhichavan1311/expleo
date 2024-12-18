
import os
print("Current working directory:", os.getcwd())

#Reading the entire file content

with open("file.bin", "r") as file:  # Adjusted relative path from current working directory
    content = file.read()
    print(content)


with open("d:/Before sunfire/Technocirrus/Technocirrus/training/expleo/file.bin", "r") as file:
    content = file.read()
    print(content)


#Overwriting content in a file

with open("file.bin", "w") as file:  # Open the file in write mode
    file.write("This is the new content of the file.\n")  # Write new content


with open("file.bin", "r") as file:  # Open the file in read mode
    content = file.read()  # Read the entire content of the file
    print(content)  # Print the content of the file


'''Example Output:
Current working directory: D:\Before sunfire\Technocirrus\Technocirrus\training\expleo
Hello, binary world!
Hello, binary world!
This is the new content of the file.
'''