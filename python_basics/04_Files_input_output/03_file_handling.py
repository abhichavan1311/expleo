# #Deleting a File
# import os

# os.remove("abhishek.txt")
# print("File deleted successfully.")

# #output: File deleted successfully.

# #Copying a File
# import shutil

# shutil.copy("python_basics/file_renamed.bin", "file_renamed.bin")
# print("File copied successfully.")

# #Output:File copied successfully.


# #Checking if a File Exists
# import os

# print("Current working directory:", os.getcwd())

# if os.path.exists("python_basics/file_renamed.bin"):
#     print("The file exists.")
# else:
#     print("The file does not exist.")

# #Output:The file exists.

#Writing JSON Data to a File
import json

data = {"name": "Alice", "age": 25, "city": "New York"}

with open("data.json", "w") as file:
    json.dump(data, file)
    print("JSON data written to file.")

#Output:JSON data written to file.

#Reading JSON Data to a File
import json

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

#Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}




    


