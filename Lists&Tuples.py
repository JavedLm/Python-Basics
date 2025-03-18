#Lists and tuples are equivalents of arrays in python
#Built-in data types that store set of values. Can store elements of different types
marks = [98,99,87,76,56,77,89]      #list in python     #in other programming languaues the data should be of a single type whereas in python it's not the case
print(marks)
print(type(marks))
print(marks[3])
print(marks[0])
print(len(marks))

#Strings are immutable (Can't be changed), whereas lists are mutable in Python.

str = "hello"
print(str[0])
# but str[0] = "y" is an illegal operation for strings, but 

student = ["Javed", 85.5, "Delhi"]
print(student[0])
student[0] = "Sahil"                # this is possible for lists

#List slicing       list_name[starting_index : ending_index]       Here also ending index not included
marks = [98,99,87,76,56,77,89] 
print(marks[1:4])           #ending index not included
print(marks[:4])            #from begining till index 4
print(marks[1:])            #also can be written as marks[1:len(marks)]
print(marks[-3:-1])         #-1 will not be included

#Lists Methods/mutation in lists        These commands return None when they are given the print command directly.
list = [2,1,3,1]                       #list = [mango, banana, litchi]    These will also be sorted in alphabetical order when given the reverse command
list.append(4)                       #adds one element at the end
print(list)                 
list.sort()                         #sorts in ascending order
print(list)
list.sort(reverse = True)           #sorts in descending order
print(list)
list.reverse()                      #reverse lists
print(list)
list.insert(0, 5)                   #insert element at list #list.insert(index,element to be inserted)
print(list)
list.remove(1)                      #removes the first occurance of the element    list.remove(the number to be removed)
print(list)
list.pop(3)                         #removes element at the index   list.pop(index)
print(list)

#Tuples are built-in data types that let us create immutable (can't be changed just like strings) sequences of values

tup = (2,1,3,1)
print(type(tup))
print(tup[2])
# tup[0] = 5   #not allowed in tuples assigning or changing not allowed
#to clarify a tuple to python you must add a comma in a single tuple case or else it considers it as an integer     tup(1,) and not tup(1)
print(tup[1 : ])                #Tuple slicing is also possible

#Tuple methods
"""tup = (2,1,3,1)
print(tup.index(3))             #prints the index of the first occurance of desired input element
print(tup.count(1))             #prints the occurance of an input element in a tuple"""

#WAP to ask the user to input 3 of their fav. movies and store them as a list
mov1 = input("Enter your first favorite movie : ")              #movie = []                                                     #movies = []
mov2 = input("Enter your second favorite movie : ")             #mov1 = input("Enter your first favorite movie : ")             #movies.append(input("enter 1st movie : "))
mov3 = input("Enter your third favorite movie : ")              #mov2 = input("Enter your second favorite movie : ")            #movies.append(input("enter 2nd movie : "))
list = [mov1, mov2, mov3]                                       #movies.append(mov1)                                            #movies.append(input("enter 3rd movie : "))
print(list)                                                     #movies.append(mov2)                                            print(movies)
                                                                #print(movies)

#WAP to check if  a list contains a palindrome of elements (list from the front and back are the same)      Using copy() method
list = []
num1 = int (input("Enter the first number :"))
num2 = int (input("Enter the second number :")) 
num3 = int (input("Enter the third number :"))
num4 = int (input("Enter the fourth number :"))
num5 = int (input("Enter the fifth number :"))
list.append(num1)
list.append(num2)
list.append(num3)
list.append(num4)
list.append(num5)
print(list)

copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("It's a Palindrome.")
else:
    print("Not a Palindrome.")

#WAP to count the number of students with grade "A" in the tuple
tup = ("C", "D", "A", "A", "B", "B", "A")
print(tup.count("A"))

#WAP to store the above values in a list and sort them in ascending order
list = ["C", "D", "A", "A", "B", "B", "A"]
list.sort()
print(list)

#04:08:00