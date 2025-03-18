class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student (86, 87, 89)
print(stu1.percentage)

#Now consider the case if there was an error in the input marks and the teacher wants to change it

stu1.phy = 86
print(stu1.phy)                 #this value changes
print(stu1.percentage)          #this value remains the same as above

#to update this we add another function in line 7 #def calcPercentage(self):
# self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
#and then call and print this function seperately using stu1.calcPercentage() and Print(stu1.Pencentage)

#Rather we use PROPERTY DECORATOR for this above problem in a simpler way
#Used in any method in a class to use method as a property
# @property
#  def percentage(self):
#  return str((self.phy + self.chem + self.math) / 3) + "%"


#POLYMORPHISM (when the same operator is allowed to have diff meaning acc to context) (Eg: Operator Overloading)
#Eg: print(1+2)
#print("Javed" + "Khan")  #concatenation
#print([1,2,3] + [4,5,6])           #O/p [1,2,3,4,5,6]

#Class to create complex numbers and add them

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i+", self.img, "j")

    def add(self, num2):                        #changes made here
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)


num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,2)
num2.showNumber()

num3 = num1.add(num2)           #To avoid writing this we make the chnages in line 43 (__add__)(dunder function) and we can replace this line as num1+num2
num3.showNumber()

#Operator and Dunder functions
#Addition               a+b --->    a.__add__(b)
#Subtraction            a-b --->    a.__sub__(b)
#Multiplication         a*b --->    a.__mul____(b)
#Division               a/b --->    a.__truediv____(b)
#Modulus                a%b --->    a.__mod____(b)

#09:49:00

#Circle class with radius 'r' using constructor. define Area() method of class and also Perimeter() method

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(20)
print(c1.area())
print(c1.perimeter())

#Employee class with attributes role, deptt and salary. also has a showDetails() method. Create an Engineer class inheriting properties from the Employee and has additonal attributes of name and age

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role = ", self.role)
        print("dept = ", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name 
        self.age = age          #Assuming fixed salary for all the departments
        super(). __init__("Engineer", "IT", "75000")

engg1 = Engineer("Javed", 26)
engg1.showDetails()

e1 = Employee("Acc", "Finance", 60000)
e1.showDetails()

# Class called Order which stores Item and it's price. Using Dunder Function __gt__() (greater than)to convey that order1>order2 if price(O1)>price(O2)

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):                 #Dunder Function for greater than
        return self.price > odr2.price


odr1 = Order("Chips", 50)
odr2 = Order("Tea", 30)

print(odr1 > odr2)   

#09:59:00