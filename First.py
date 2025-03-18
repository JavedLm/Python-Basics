print("Hello Javed")
print("hello","javed")
print("hello")
print("Javed")
name = "Javed" #declaration of a variable #in this case a string (always use double quotes)
age = 23
value = 100.01 #this doesn't imply that LHS=RHS (like in maths), rather means '100' is being stored/assigned to the variable value (ASSIGNMENT OPERATOR)
print("Name") #double quotes prints the content inside as it is
print(name)  #printing a variable
print("my name is :", name)
age256 = age
print(age256)
print(type(name))  #data type of variable (Integers,string,float,boolean,none)
print(type(age))
print(type(value))
#reserved words (and,as,assert,break,class,continue,def,del,elif,else,except,fianlly,False,for,from,global,if,import,in,is,lambda,nonlocal,None,not,or,pass,raise,return,True,try,with,while,yield)
#not to be used as variable names
#case sensitive language, typed implicit language (no need to define the variable type additionally)
a = 5
b = 6
sum = a+b
print(sum)
#punctuators (organize the code) (),{},@,[],#
#string and numeric values can operate together with (*)
A,B = 2,3
Text = "@"
print (2*Text*3)  # @ is printed 6 times
#string and string can operate with a (+)       #Technically known as concatenation
A,B = "2",3 # ! 2 is a string here !
Txt = "@"
print((A+Txt)*B)  #According to BODMAS #output is 2@ and not 2+@ due to the rule of joining the strings

A,B= 2,3        #Arithmetic expression between integer and float will give float as resultant 3*25.0 = 75.0
C=4             #Resultant of division operator is a float value
print(A+B*C)    

A,B = 1.5,3     #integer division between float and int displayed as a float #integer division is however meant to give integer value as resultant
C = A//B        #integer division operator (0.5 -- 0, 0.4 -- 0, 0.9999 -- 0, 1.2 -- 1) brings down the result to the nearest lowest value
print(C)        #integer division result # A//B has the same result as the floor operator # floor(1.2)=1 floor(7.99)=7 floor(-5.6)= -6
print(A/B)      #normal division result   

#remainder operator num/denom = +/+ = +; -/- = +; -,+ = +; +/- = - result turns out negative in case of a negative denominator

"""This is a  #triple quotes for a moultiple line comment
a multi-line
comment."""

#inputs in python (accept values from the user)
name = input("name : ")     #string input
print(name)                 #prints your input provided
age = int(input("age : "))
price = float(input("price : "))

print("My name is", name, "and I am", age, "years old", "and the price of apples is", price)

# a**b = a^b (logical operator in python)
# and, or , not are the logical operators in python     # in, not in are membership operators in python
#order precedence of logical operators          not > and > or 

#conditional statements     if-elif-else (SYNTAX)       #python is a langauage with imdentation (spacing is very important)
"""if(condition):
    Statement1                          #most prominently 4 spaces with the gap
elif(condition):
    statement 2
else:
    statement 3"""

light = input("light : ")       #variable decleration   #traffic light example
if (light == "red"):
    print ("STOP")
elif(light == "yellow"):
    print("LOOK OUT LOOK OUT")          #You can also add "and" as a conditional statement to fulfill various conditions simultaneously
elif(light == "green"):
    print("GOOOOOOOOOO")
else:
    print("BROKEN AF")