#del keyword (delete object properties or the entire object itself)

#Syntax
# del s1.name (for deleting attributes)
# del s1 (for deleting object)

#Private attributes and methods (for sensitive information and cannot be accessed outside the class generally by the user) (done by adding 2 underscores in front of the attribute)
#Meant to be used only within the class and not accessible form outside the class

class Account:
    def __init__(self,acc_no, acc_pass):
        self.acc_no = acc_no                    #PUBLIC
        self.__acc_pass = acc_pass              #PRIVATE

    def reset_pass(self):
        print(self.__acc_pass)                  #Since this function exists inside the class therefore the value of __acc_pass can be printed

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
# print(acc1.__acc_pass)      #Not accessible since it's inside the class and private will showcase an error in terminal
print(acc1.reset_pass())    #This won't showcase any error since it's function was inside class

# class Person:
#     __name = "Anonymous"

#     def __hello():
#         print("Hellooooooooo")

# p1 = Person
# print(p1.__name)
# print(p1.__hello)                   #these both cases will throw an error since it's all privatized

#HOWEVER
class Person:
    __name = "Anonymous"

    def __hello(self):
        print("Hellooooooooo")

    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())             #this is completely vlaid and won't throw any error since it is being accessed by a class within a program and not an external user.

#INHERITANCE (one class(child) derives the properties and methods of another class(parent)) Eg: car (Parent) and Toyota car(child)

class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("Fortuner") 
car2 = ToyotaCar("Ranger")

print(car1.name)
print(car1.start())          #Wont throw an error since inheritance is used and the properties are carried forward with each running function

#TYPES (SINGLE, MULTI-LEVEL, AND MULTIPLE INHERITANCE)

class Cars:
    @staticmethod                       #MULTi-LEVEL Inheritance                                                 
    def start():
        print("VROOOOOOOOOOM")

    @staticmethod
    def stop():
        print("car stopped")

class BMWCar(Cars):
    def __init__(self,brand):
        self.brand = brand


class M5(BMWCar):
    def __init__(self, type):
        self.type = type

car5 = M5("540HP")
car5.start()

#Multiple inheritance (there can be multiple base classes whose properties are being derived by a child class )

class A:
    varA = "Welcome A"

class B:
    varB = "Welcome B"

class C(A,B):
    varC = "Welcome C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)

#SUPER method (used to access the methods of parent class)

class Cars:
    def __init__(self,type):
        self.type = type

    @staticmethod                                                                      
    def start():
        print("VROOOOOOOOOOM")

    @staticmethod
    def stop():
        print("car stopped")

class BMWCar(Cars):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()
    
car5 = BMWCar("540HP", "Petrol")
print(car5.type)

#09:17:00

#Class method(bound to the class and receives the class as an implicit first argument)
# Static methods cant access or modify class state and generally for utility.

class Person:
    name = "anonymous"

    def changeName(self,name):
        self.name = name
    
p1 = Person()
p1.changeName("Javed Khan")         #Swaps anonymous to Javed Khan
print(p1.name)
print(Person.name)                  #This itself hasn't changed the orignal (class) attribute rather created new attribute inside an object for the completion of the task

#SO to chnage the class attribute we use Person.name in 140 or self.__class__.name for the same task.A

#To acess the function directly into our class we use class method
# @classmethod                      decorator directly changes the class attributes
# def changeName(cls,name):
#     cls.name = name

#1. Static methods ()
#2. Class methods (cls)
#3. Instance methods (self)

#09:25:00