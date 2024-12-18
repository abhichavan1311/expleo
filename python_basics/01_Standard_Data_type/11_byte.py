# Bytes Example
byte_data = b"Hello"
print(f"Byte Data: {byte_data}")
print(f"Decoded: {byte_data.decode()}")
print(f"Length: {len(byte_data)}")

#Actual_use
'''Reading and writing binary files,Cryptography and Hashing,Encoding and Decoding Data,Interfacing with External APIs'''
import hashlib

data = b"Hello, world!"
hashed_data = hashlib.sha256(data).hexdigest()
print(hashed_data)  # Output: The SHA-256 hash of the data as a string



'''Example Output:
PS D:\Before sunfire\Technocirrus\Technocirrus\training\expleo> & "C:/Users/Abhishek Chavan/AppData/Local/Microsoft/WindowsApps/python3.11.exe" "d:/Before sunfire/Technocirrus/Technocirrus/training/expleo/python_basics/01Standard_Data_type/11_byte.py" 
Byte Data: b'Hello'
Decoded: Hello
Length: 5
315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3
PS D:\Before sunfire\Technocirrus\Technocirrus\training\expleo> 
'''