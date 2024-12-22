
# import os
# newfile=open('abhishek.txt','w+')

# for i in range(0,10):
#     newfile.write('\n Hello abhi')

# #######################


import os
newfile=open('abhishek.txt','r')

for i in range(0,10):
    newfile.seek(0)  # Reset the file pointer to the beginning
    print(newfile.read())

