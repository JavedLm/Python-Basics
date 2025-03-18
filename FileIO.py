#Python can be used to perform operations on a file (Read/Write)
#Text files(.txt, .docx, .log) -- in character formats, and Binary Files (.mp4, .mov, .png, .jpeg)

# 1. Opening a file  f = open("file_name", "mode")      By default the mode is read (r) or else is selected by the user. Eg: open for writing (w) truncating the file first
# (r) read 
# (w) open for writing (overwrites the file generally by deleting the existing data)
# (x) create a new file and open it for writing 
# (a) open for writing, appending to the end of file if it exists (not deleting the existing contents and adding additional ones)
# (b) binary mode 
# (t) text mode  (default) (not necessary to write "rt" if reading a text file only "r" is enough, "t" is default)
# (+) open a disk file for updating (R/W)

# Eg: r mean only read, but if we write r+ or t+ it will operate read and write both
# r+ READ+OVERWRITE (POINTER AT THE BEGINNING) --- NO TRUNCATION
# w+ READ+OVERWRITE (Pointer doesn't make sense here since the whole data disappears due to truncate operation) -- TRUNCATE
# a+ READ+APPEND (Pointer at the end) --- NO TRUNCATION

f = open("demo.txt", "r")       #This will display the contents of the file in the terminal. Storage path of file might be relevant in case of other folder.
data = f.read()                 #Reads the data of the file (Read operation)

#But if we put data = f.read(6) then the first 6 characters of the text including spaces will be printed
# data = f.readline()  Reads one line at a time
#readline cannot be executed after read opeartion since the whole data is already been analyzed by the read and there will be empty spaces in the terminal (if readline is executed)

print(data)                     #prints the data
print(type(data))               #prints the type of data
f.close()                       #command to close the file

#WRITING TO A FILE
# f = open("demo.txt", "w")         'w' operation
# f.write("this is a new line")     overwrites the existing data completely and only this satement is printed in the text file

# f = open("demo.txt", "a")         'a' operation
#f.write("this is a new line")      adds this line to the file (changes made in text file)

#Python creates a new file for you automatically if you pass a write or append statement in the code 'w' or 'a' with the file name.

#'with' Syntax
#with open ("demo.txt", "a") as f:
    #data = f.read()

#for installing a new system we can use pip (Package installer for python). Eg: pip install tensorflow  or pip3 install tensorflow (for different version)

#DELETING A FILE using the os module 
# import os
# os.remove("filename")

#PRActice question
with open("practice.txt", "w") as f:
    f.write("Hello.\n I am Javed Khan\n")
    f.write("Here to learn\n Java")

#SWAP Java to Python in above program
with open("practice.txt", "r") as f:
    data = f.read()
new_data = data.replace("Java", "Python")
print(new_data)

# with open("practice.txt", "w") as f:            #Makes changes to the orignal file replacing Java with python
#     data = f.write()

#Searching weather the word "learning" exisats in the file or not
def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if (data.find(word) != -1):
            print("found")
        else:
            print("not found")
    
check_for_word()

#WAF to find in which line of the file does the word "learning" occur first. Print -1 if not found

def check_for_line():
    word = "learning"
    data = True             #Initialized to make to loop run. or else it won't function
    line_no = 1
    with open("demo.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

print(check_for_line())

#From a file containing numbers seperated by comma, print the count of even numbers

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)             #the program till here will print the data in string format at the terminal and no conclusion about even or odd

#Further we have to pick up individual numbers, convert them to integers (Parsing/ casting them to int), and sort them by odd/even

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)  

#     num = ""
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(int(num))
#             num = ""
#         else:
#             num += data[i]        Using general concept without the SPLIT predefined fucntion in Python

#Using Split function 
count = 0
with open("demo.txt", "r") as f:
    data = f.read()
    
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)