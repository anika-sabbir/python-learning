#License Eligibility(Write a program to check if a person can apply for a driving license.)
age =24
if(age>=18):
    print("can apply for lilcense")


#Traffic Light(Write a program to display action based on traffic light color.)
light = "green"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")

print("end of code")

#Voting Eligibility(Write a program to check if a person can vote.)

age=16

if(age>=18):
    print("can vote")
else:
    print("cannot vote")

#Student Grade(Write a program to display grade based on marks.)
marks = int(input("enter student marks : "))
if(marks >= 90):
    grade="A"
elif(marks >=80 and marks <90):
    grade="B"
elif(marks >=70 and marks <80):
    grade="C"
else:
    grade="D"
    print("grade of the student ->",grade)


#Nesting
age=30
   
if age >= 18:
        if age >= 16:
         print("cannot drive")
        else:
         print("can drive")


#write a programme to check if a number entered by the user is odd or even.
num=int(input("enter the number"))
rem = num%2
if(rem == 0):
    print("Even")
else:
    print("Odd")


# write a programme to find greatest of 3 numbers entered by the user.
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
if(a>=b and a>=c):
    print("first number is largest",a)
elif(b>=c):
    print("second number is largest", b)
else:
    print("third is largest",c)

#write a programme to check if a number is a multiple of 7 or not.
x=int(input("enter number:"))
if(x% 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")


