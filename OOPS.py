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