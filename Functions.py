#Ends with Function Example (gives a boolean response)  str.endswith()

str = "My name is Javed Khan"
print(str.endswith("an"))

"""Similarly
str.capitalize()            Capitalizes first character. Works only one time. Doesn't change the orignal string.
str.replace("old","new")    Replaces the desired characters in the string. Eg: P--J
str.find(" ")               Returns the first index of the first occurance of character in a string.
str.count("")               Counts the occurance of a particular character in a string.
Generally negative indices don't exist rather than in the concept of negative slicing. So -1 is an invalid index.
"""
#Program to input user's first name and print it's length
name = input("What is your name?\n")
print("Hello ", name, ". The length of your name is: ", len(name))

#WAP for the occurance of € in a string
str = input("Enter the characters : \n")
print (str.count("€"))

#Indentation is very important in Python. 4 spacing after the if loop is necessary and must be done by user

#Nesting (Eg: if within an if statement)                #WAP for driving
age = int(input("Please enter your age : "))
if(age>=18):
    if(age>=80):
        print("Sorry, but you cannot drive.")
    else:
        print("Congrats, you can drive.")
else:
    print("Sorry, you cannot drive.")

#WAP for odd or Even

num = int(input("Please enter a number :"))
if(num%2 == 0):
    print("The number you entered is even.")
else:
    print("The number you entered is odd.")

#WAP for greatest among 3 numbers

num1 = int(input("Please enter 1st number :"))
num2 = int(input("Please enter 2nd number :"))
num3 = int(input("Please enter 3rd number :"))
if(num1>num2):
    if(num1>num3):
        print("num 1 is the greatest number.")
    elif(num2>num1):
        if(num2>num3):
            print("num2 is the greatest number.")
else:
    print("num3 is the greatest number.")

"""if (a>=b and a>=c):
    print("a is greatest")
   elif(b>=c):
    print("b is greatest")
   else:
    print("c is the largest.")"""

