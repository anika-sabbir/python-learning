#Creating Class and object
class Student:
    name = "Anika"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)

#Creating Class and object
class Car:
    colour = "Black"
    brand = "mercedes"

car1 = Car()
print(car1.colour)
print(car1.brand)

#__init__ function
class Student:
    name = "Anika"
    def __init__(self):
     print("adding new student in database..")
    

s1 = Student()

#__init__ function
class Student:
   #default constructors
   def __init__(self):
      pass
  #parameterized constructors   
   def __init__(self,name):
     self.name = name
     print("adding new student in database..")
    

s1 =Student("Anika")
print(s1.name)

s2 =Student("Iqra")
print(s2.name)

#class and instance attributes
class Student:
   college_name = "ABC College"
   def __init__(self,name):
     self.name = name
     print("adding new student in database..")
    

s1 =Student("Anika")
print(s1.name)

s2 = Student("Iqra")
print(s2.name)

print(Student.college_name)
#Creating class and instance attributes
class Student:
   college_name = "ABC College"

   def __init__(self,name):
     self.name = name
   def welcome(self):
    print("welcome student")


s1 =Student("Anika")
s1.welcome()
#Q.Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.
 
class Student:
   def __init__(self,name,marks):
      self.name = name
      self.marks = marks
   def get_avg(self):
      sum=0
      for val in self.marks:
         sum += val
      print("hi",self.name,"your avg score is",sum/3)
s1 = Student("Anka",[99,98,97])
s1.get_avg()

#Static Method
class Student:
   def __init__(self,name,marks):
      self.name = name
      self.marks = marks
   @staticmethod
   def hello():
      print("hello")
   def get_avg(self):
      sum=0
      for val in self.marks:
         sum += val
      print("hi",self.name,"your avg score is",sum/3)
s1 = Student("Anka",[99,98,97])
s1.get_avg()
s1.hello()
# Abstraction
class Car:
   def __init__(self):
      self.acc = False
      self.brk = False
      self.clutch = False
   def start(self):
      self.cluch = True
      self.acc = True
      self.brk = True
      print("car started..")
car1 = Car()
car1.start()
#Create Account class with 2 attributes - balance & account no.Create method for debit,credit & printing the balance.

class Account:
   def __init__(self,bal,acc):
      self.balance = bal
      self.account_no = acc
   
   def debit(self,amount):
      self.balance =- amount
      print("TK.",amount,"was debited")
      print("total balance =", self.get_balance())

   def credit(self,amount):
      self.balance += amount
      print("TK.",amount,"was credited")
      print("total balance =", self.get_balance())
   def get_balance(self):
      return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)


#private attributes and method
class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()
p1.welcome()

#Inheritance
class Car:
   @staticmethod
   def start():
      print("car started")

   @staticmethod
   def stop():
      print("car stoped")

class ToyotaCar(Car):
   def __init__(self,name):

      self.name = name
car1 = ToyotaCar("fortune")
car2 = ToyotaCar("pirus")

print(car1.name)

#single,Multilevel inheritance
class Car:
   @staticmethod
   def start():
      print("car started")

   @staticmethod
   def stop():
      print("car stoped")

class ToyotaCar(Car):
   def __init__(self,brand):
      self.name = brand

class Fortuner(ToyotaCar):
   def __init__(self,type):
      self.type =type
car1= Fortuner("diesel")
car1.start()

#Multiple Inheritance
class A:
   varA = "welcome to a class A"

class B:
   varB = "welcome to a class B"

class C(A,B):
   varC ="welcomr to a class C"

c1 =C()

print(c1.varC)
print(c1.varB)
print(c1.varA)

#Super method
class Car:
   def __init__(self,type):
      self.type = type
   @staticmethod
   def start():
      print("car started")

   @staticmethod
   def stop():
      print("car stoped")

class ToyotaCar(Car):
   def __init__(self,name,type):
      super().__init__(type)
      self.name = name
      super().start()

car1 = ToyotaCar("pirus","electric")
print(car1.type)

#class method
class Person:
   name = "anonymous"
   def changeName(self,name):
      self.__class__.name ="Anika"

p1 =Person()
p1.changeName("Anika")
print(p1.name)
print(Person.name)

#property
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)

#polymorphism
class Complex:
     def __init__(self, real, img):
        self.real = real
        self.img = img

     def showNumber(self):
        print(self.real, "i +", self.img, "j")

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

#
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNumber()


num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

#Q.Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
#Define a parimeter()method of the class which allows you to calculate the perimeter of the circle.

class Circle: 
   def __init__(self,radius):
    self.radius = radius

   def area(self):
      return (22/7) * self.radius **2
   
   def perimeter(self):
      return 2 *(22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

#Q.Define a Employee class with attributes role,department & salary.This class showDetails()method
#Createan Engineer class that inherits properties from Employee & has additional attributes:name & age
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

engg1 = Engineer("Elon Musk", 40)
engg1.showDetails()
#Q.Create a class called Order which stores item & its price.Use Dunder function_gt__() to convey that:
#order1 > order2 if price of order1 > price of order2
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price

odr1 = Order("chips", 20)
odr2 = Order("tea", 15)

print(odr1 > odr2)