""" AND                     OR
T T -- T                T T -- T    
F T -- F                T F -- T
T F -- F                F T -- T
F F -- F                F F -- F """

# Combinations for conditional statements   if -- elif -- else,  if -- elif, if dependent on the use case

#single line conditional statements/ Ternary operators
# <var> = <value1> if <condition> else <value2>  (when the if condition is satisfied the <var> takes value1 else value2)            CASE1

food = input ("food : ")
eat = "Yes" if food == "cake" else "no"
print(eat)

# <statement1> if <conditon> else <statement2>              CASE2

food = input("food :")
print("sweet") if food == "cake" or food == "jalebi" else print ("not sweet")

# CLever if / Ternary operator 
# <var> = (false_value, true_value) [<condition]

age = int (input ("age :" ))
vote = ("no", "yes") [age >= 18]
print(vote)

salary = float(input("salary :"))
tax = salary*(0.1, 0.2) [salary >=50000]
print(tax)

""" name = input ("name : ")
    print(name)
Can also be written as: print(input("name : ")) """  #but avoid this 

# shortcut for commenting multiple lines easily is: Ctrl+/

#Operators
# Arithmetic (+, -, *, /, %, **)                                %= modulo/remainder operator  **= power operator (a^b)
# Relational/ Comparision operators (==, !=, >, <, >=, <=)      #Gives output as a boolean, generally compares the 2 values. a=50, b=20, print (a==b) -- Answer =False
# Assignment operators (=, +=, -=, *=, /=, %=, **=)             (num = num+10) OR (num += 10)   Eg: num =10, num =num+10, OR num += 10; result = 20 
# Logical operators (and, not, or)                              

#Type Conversion (Automatic) and Type Casting (manual conversion)
a=2
b=4.25
sum=a+b
print(sum)   #actually is 2.0+4.25 = 6.25 Automatic/implicit conversion

#Normally we cannot add string and float values in an expression together. However it is possible through Type casting

a,b = 1, int("2")    #type casting
print (a+b)
print(type(b))

#input() , int(input()) , float(input())  from the user via keyboard while running the program, also this value from the user is always considered as a string irrespective of the orignal type.
# therefore the casting is used eg: int(input())