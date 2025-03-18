#Object Oriented programming (OOP) in Python
#To map real world scenarios, we code objects in code.
#Class is the blueprint for creating objects. Eg: A group of students inside the class. (students act as objects)
#creating class
class Student:              #Generally with a capital letter
    name = "Javed Khan"     #This value will be printed for all objects in the class
    city = "New Delhi"

#creating object (instance)
s1 = Student()
print(s1.name)              #Prints the exact name in the class
print(s1.city)

s2 = Student()
print(s2)                   #prints the location and type of the class

#CONSTRUCTOR or __init__() Function (always Executed when object is being initiated)
#This is created and executed by default from Python even if you dont specify or initilize it.

class Student:

    college_name = "Jamia Hamdard"   #This is a class attribute (stored only once in a memory)

    #Default constructor (Just self)
    def __init__(self):
        pass
    
    #Parametrized constructors (additional references)
    def __init__(self, fullname, marks):       #Self parameter is a reference used to the current instance of the class, and is used to access variables that belongs to the class.
        self.name = fullname                    #This is actually an instance atttribute since diff. students have diff.names in a class
        self.marks = marks                      #Also an instance attribute defined using self.______. Self is actually a reference for the object.
        print("creating new student in database.")

s1 = Student("Javed's", 98)
print(s1.name, s1.marks)

s2 = Student("Sahil's", 100)
print(s2.name, s2.marks)              #The data or variables stored inside the program are called as attributes
print(s2.college_name)

#Class Attributes(same for every object in the class)(Eg: same college name for a group of students) and Instance/object/data (varies for every object) Attributes
#Instance attribute is stored multiple times in a memory
#Obj. Attr >> Class Attr. prioritization (in case of a simlar name for both attributes)

#METHODS (functions belonging to the objects)
#EG: CAR-- ENGINE,FEATURES ETC. are attributes and How does it function is a METHOD

class Car:
    
    def __init__(self, name, mileage):      
        self.name = name                    
        self.mileage = mileage                    
        print("creating new car in database.")

    def welcome(self):
        print("Welcome to,", self.name)

s1 = Car("BMW", 9.8)
print(s1.name, s1.mileage)

#Create a class that takes name and marks of 3 subjects as arguments in a constructor. And a method to print the average

class Marks:
    college_names = "AIIMS"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("creating a new transcript in database.")

    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("Welcome, ", self.name, "your average score is:", sum/3)

s1 = Marks("Javed", [78 , 89, 90])
s1.get_avg()

s1.name = "Sahil_Khan"              #If attribute is desired to be chnaged the same value of avg will be printed for this new name also
s1.get_avg()

#STATIC METHODS (don't use the self parameter and work at class level) (Generally self parameter issued for object level)

class Students:     #decorator changes the behavior of normal function
    @staticmethod   #This is a decorator (allowing us to wrap another function in order to extend the behavior of wrapped function without permanently modifying it)
    def hello():
        print("Hello")

s3 = Students()
s3.hello()

# 4 Pillars of OOPS

#ABSTRACTION (hiding the implementation details of a class and only showing necessary features to the user)

class Auto:
    def __init__(self):
        self.acc = False            #INITIALIZATION
        self.clutch = False
        self.brake = False

    def start(self):
        self.clutch = True      #This can be an eg of abstraction where all the intermediatre steps are not displayed on the terminal instead th efinal and necessary o/p is given)
        self.acc = True         #CONDITIONS
        print("Car Started........ VROOOOOOOOOOM")

car1 = Auto()           #CALLING FUNCTIONS
car1.start()            #OUTPUT

#Encapsulation (wrapping data and related functions into a single unit (object)) (consider it with a RL CAPSULE EG) (The whole code is an encapsulation eg)

#Inheritance()

#Polymorphism()

#Create an account class with 2 attributes (balance and account number). Create methods for debit, credit and printing the balance

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.acc_no = acc

#debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount, "was debited form your account")
        print("total balance =", self.get_balance())

#credit method
    def credit(self,amount):
        self.balance += amount
        print("Rs.", amount, "was credited to your account")
        print("total balance =", self.get_balance())

    def get_balance(self):          #for the final value
        return self.balance

acc1 = Account(10000, 123456)   #10k in the amount in the account and 123456 is the account number
acc1.debit(1000)
acc1.credit(4000)

print(acc1.balance)
print(acc1.acc_no)

#08:51:00