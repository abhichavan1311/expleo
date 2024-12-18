# Open the file in write mode, write content, and then read and print the content
with open("file.bin", "w+") as file:  # Use "w+" mode to allow both writing and reading
    file.write("Hi Joey,How are you doing?\n")  # Write new content
    
    # Move the file pointer back to the beginning of the file after writing
    file.seek(0)
    
    # Read the content and print it
    content = file.read()
    print(content)  # Print the content of the file


#Appending to a File
# Open the file in append and read mode
with open("file.bin", "a+") as file:
    file.write("Abhishek: I am fine joey, where is chandler ?\n")  # Add new content at the end
    
    # Move the file pointer back to the beginning to read the content
    file.seek(0)
    
    # Read the entire content and print it
    content = file.read()
    print(content)  # Print the content of the file

#Changing the name of a file
import os

os.rename("file.bin", "file_renamed.bin")
print("File renamed successfully.")

#Moving a file to a new directory

import shutil

shutil.move("file_renamed.bin", "python_basics/file_renamed.bin")
print("File moved successfully.")




'''Example Output:
Hi Joey,How are you doing?

Hi Joey,How are you doing?
Abhishek: I am fine joey, where is chandler ?

File renamed successfully.
File moved successfully.
'''