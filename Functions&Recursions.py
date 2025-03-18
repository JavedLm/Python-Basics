#Block of statements performing a specific task (unlike a loop (countable) this can be used multiple times to perform a specific task infinitely)
#avoids repeatability in the code (redundancy) Eg: #WAP to calcultate the sum of 2 numbers multiple times with different values at various places in the code

#Syntax: 
# def func_name(param1, param2) :        param1,param2 can be the input values from the user
#Some work
#return val
#func_name(argument1,argument2)                 #calling the function (arguments are the same values which are received or linked with parameters)
                                                #we can also say that the values of arguments are stored in the parameters
def calc_sum(a,b):
    sum = a+b
    print(sum)
    return sum
calc_sum(5,10)
calc_sum(2,34)
calc_sum(87,56)

def print_hello():                  #No requirements of assigning parameters since we only reqd a single string value to be printed
    print("Hello")

print_hello()                       #this statement (arguments) just assigns the number of times an output should be printed
print_hello()

def print_hello():
    print("Hello")

output = print_hello()
print(output)               #The output is none since this function doesn't return any value itself. (no parameters and no return)

#WAP to calculate the average of 3 numbers
def calc_avg(a,b):
    avg = (a+b)/2
    print(avg)
    return avg
calc_avg(90,60)
calc_avg(5,5)

#Different types of functions in Python
#Built in functions (print(), len(), type(), range()) and User defined functions ()

print("Electrical Engineering", end = " ")
print("Javed Khan")                         #Instead of printing on different lines, this will beprinted on the same with a gap as defined by our end variable

#Default parameters (Assigning a default value to a parameter, used when no argument is passed)
def cal_prod(a, b=2):           #the value of b here is said to be a default parameter
    prod = a*b
    print(prod)
    return prod
cal_prod (3)        

#WAF to print the length of the list
numbers = [1,2,3,4,5,6,7]
movies = ["KGF", "DON", "DON2"]

def len_list(list):
    print(len(list))

len_list(numbers)
len_list(movies)

#WAF print elements of a list in a single line
numbers = [1,2,3,4,5,6,7]
movies = ["KGF", "DON", "DON2"]

def len_list(list):
    for items in list:
        print(items, end= " ")

len_list(movies)

#WAF to find the factorial of 'n' (n is parameter)

n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
    print(fact)

#Embedding this logic in a function

def calc_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
        print(fact)
calc_fact(6)

#WAF to convert EUR to INR

def converter(eur_val):
    inr_val = eur_val * 90
    print(eur_val, "EUR =", inr_val, "INR")

converter(2)

#WAF for an input number returning "ODD" or "EVEN" based on the input number

def cal_OE(n):
    if (n%2 == 0):
        print("EVEN")
    else:
        print("ODD")
cal_OE(5)


#06:36:40

#RECURSION (When functions call itself repeatedly)
#In case of functions we used a statement to call our function whenevr we need it (calculating sum)
#But for the case fo Recursion the functions call themselves repeated number of times (just like loops but instead recursions have self calling process)
#Loops and recursion are interrelated and interchangable (can do tasks of each other with the same concept)

#WAF using recursion to print the sequence backwards from a number

def show(n):       # --> 1
    if(n == 0):    #this loop is really important in this condition or else the call for the function goes on infinitely ----> called as "Base case"
        return     #seq of code is 5 4 3 2 1. this return function will go 0 1 2 3 4 5 once the if condition is satisfied to return the value to the initial called function.
    print(n)       
    show(n-1)

show(4)   #Call stack concept LIFO example considering above loop as an example and deleting layers consecutively.
print("END")

#EXAMPLE 
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    print("END")        #This END will be printed consecutively after extracton of each layer (running of loop) LIFO layer and box example

show(3)

#Recursion explained using factorial
#Since n! = (n-1)! * n , Example: 5! = 5*4*3*2*1 or 5*4! this is a recursive relationship.

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(4))

#WARF to calculate the sum of first n natural numbers
def sum_nat(n): 
    if(n == 1):                             #if (n == 0):
        return 1                            #return 0
    return (n+1) + n                        #return sum_nat (n-1) + n

print(sum_nat(3))

#WARF to print all the elements in a list(using index and list as parameters)

def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
    
fruit = ["A", "B", "C", "D"] 

print_list(fruit)

#07:05:30