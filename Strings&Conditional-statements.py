str1 = "This is a String."
str2 = 'Also a String.'
# str3 = """Also a String."""
#Escape sequence conunters (ESC) are used to create multiple line strings (provide formatting characters)

str4 = "This is a string.\nWe are creating in Python"  #\n called as ESC provides new line
print(str4)                                             #Also \t creates a Tab ESC creating a tab space in the output

#Concatenation  "Hello"+"World" ---- "Hello World"  (Connecting 2 Strings)
#Length of a string --- len(str)


print (len(str1))
print(len(str2))
print(str1+str2)
print(str1+" "+str2)    #Empty spaces are also calculated while counting the length of the string (Don't ignore them)
print(len(str1+str2))

#INDEXING
""" J   A   V   E   D   _   K
    0   1   2   3   4   5   6    #INDEX (Helps us to access the characters)
"""
str = "JAVED_KHAN"
ch = str[4]                        #Index number 4 --- D is located
print(ch)                          #We can access the characters by using indexing but cannot manipulate or change them by assignment operator(=) in our code

#SLICING --- Accessing part of a string 
#Syntax: str[starting_idx : ending_idx]      Ending index not included 

str = "JAVED_@#KHAN"
print(str[3 :7])
print(len(str))
print(str[5 : len(str)])            #print(str[5:]) is also valid for this case (This is implicit)

#Slicing with negative index (PYTHON SPL. CONCEPT)
#Considering the last index starting from -1

str = "JAVED_KHAN"
print(str[-4:-1])       #Here also the last index (-1)--'N' is not included