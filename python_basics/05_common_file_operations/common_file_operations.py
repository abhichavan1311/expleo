
### Indexing

my_list = [10, 20, 30]
print(my_list[0])  # Output: 10
print(my_list[1])  # Output: 20

### Slicing 
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])  # Output: (2, 3, 4)

### Concatenation

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)  # Output: [1, 2, 3, 4, 5, 6]


### Replace Item in the List 
list=['hadoop','java','python']
list[1]='android'
print(list)         #output: ['hadoop', 'android', 'python']

### delete item in the list
list=['hadoop','java','python']
del(list[2])
print(list)         #Output: ['hadoop', 'java']

### Repetetion
print([1, 2] * 3)  # Output: [1, 2, 1, 2, 1, 2]

### Length
my_string = "Python"
print(len(my_string))  # Output: 6

### Membership

my_list = [1, 2, 3]
print(2 in my_list)  # Output: True
print(5 in my_list)  # Output: False

### using pop

# Example 1: Popping the last element
my_list = [10, 20, 30, 40]
removed_element = my_list.pop()
print("Removed element:", removed_element)  # Output: 40
print("Updated list:", my_list)  # Output: [10, 20, 30]

# Example 2: Popping a specific index
my_list = [10, 20, 30, 40]
removed_element = my_list.pop(1)
print("Removed element:", removed_element)  # Output: 20
print("Updated list:", my_list)  # Output: [10, 30, 40]


### using remove

# Example 1: Removing an existing element
my_list = [10, 20, 30, 40, 20]
my_list.remove(20)
print("Updated list:", my_list)  # Output: [10, 30, 40, 20]

# Example 2: Attempting to remove a non-existing element
my_list = [10, 20, 30]
try:
    my_list.remove(50)  # Raises ValueError
except ValueError:
    print("Value not found in the list.") #Output: Value not found in the list.
