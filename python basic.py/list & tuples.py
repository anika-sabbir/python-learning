#Create a list of 5 float marks. Print the list, its type, and the first two elements separately.
marks = [94.5,86.2,76.9,67.3,55.3]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])

#Create a mixed list containing a name, marks, age, and city. Print it.
student = ["Anika",94.5,23,"Chattogram"]
print(student)

#Create the same student list. Print the first element, then update it and print the full list again
student = ["Anika",94.5,23,"Chattogram"]
print(student[0])
student[0] = "Anika"
print(student)

#List slicing:Create a marks list of 5 numbers. Print elements from index 1 to 3 using slicing.
marks = [86,54,72,43,89]
print(marks[1:4])


#From a marks list, print all elements from index 1 to the end.
marks = [86,54,72,43,89]
print(marks[1:])

#From a marks list, print elements from index -3 to -1 using negative slicing.
marks = [86,54,72,43,89]
print(marks[-3:-1])

#append method:Create a list and append a new element to it. Print the result.
list=[2,4,6]
list.append(4)
print(list)

#sort Ascending method:Create a list and sort it in ascending order. Print both the return value of sort and the list
list=[2,8,6]
print(list.sort())
print(list)

#
#sort descending method:Append to a list, then sort it in descending order. Print each step.
list=[2,8,6]
print(list.append(4))
print(list.sort(reverse=True))
print(list)

#Create a fruit list. Sort it in descending order, Print results.
list=["Mango","Orange","Apple"]
#print(list.append(4))
print(list.sort(reverse=True))
print(list)

#Create a fruit list. Sort it in aescending order, Print results.
list=["Mango","Orange","Apple"]
#print(list.append(4))
print(list.sort())
print(list)

#List reverse:Create a character list and reverse it. Print the result.
list =['a','d','g','b']
list.reverse()
print(list)

#List insert:Create a number list and insert a value at index 1. Print the result.
list =[2,1,3]
list.insert(1,7)
print(list)

#list remove:Create a list and remove the element at index 2 using pop. Print the result.
list =[2,1,3,1]
list.pop(2)
print(list)

#Write a programme to ask the user to enter names of their 3 favorite movies & store them in a list
movies = []
movies.append(input("enter 1st movie:"))
movies.append(input("enter 2nd movie:"))
movies.append(input("enter 3rd movie:"))

print (movies)
print("end of code")

#Write a programme to check if a list contains a palindrome of elements.

list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("Not palindrome")




#Problem 1 — Convert(Create a list of 5 numbers. Convert it into a tuple and print both)
number = []
number.append(int(input("enter 1st number")))
number.append(int(input("enter 2nd number")))
number.append(int(input("enter 3rd number")))
number.append(int(input("enter 4th number")))
number.append(int(input("enter 5th number")))
number_tuple=tuple(number)
print("list:",number)
print("tuple:",number_tuple)


#Problem 2 — Access(Create a tuple of 3 cities. Add them one by one into an empty list using .append().)
cities=("Chattogram","Dhaka","Sylhet")
city_list =[]
for city in cities:
    city_list.append(city)
    print("city list:",city_list)
print("end of code")

#Problem 3 — Length Compare(Create a list and a tuple each with 4 items. Print the length of both and check if they are equal.)

my_list = [1, 2, 3, 4]
my_tuple = (5, 6, 7, 8)
print("List length:", len(my_list))
print("Tuple length:", len(my_tuple))
print("Equal?", len(my_list) == len(my_tuple))

#Problem 4 — Search(Create a fruit list and vegetable tuple. Check if user input exists in either.)
fruits = ["mango", "banana", "apple"]
vegetables = ("carrot", "potato", "onion")
food = input("Enter a food item: ").lower()
if food in fruits:
    print(food, "is in the fruits list!")
elif food in vegetables:
    print(food, "is in the vegetables tuple!")
else:
    print(food, "not found in either.")



#Problem5-Combine(Create a tuple and list of 3 numbers each. Convert tuple to list and combine both.)
t = (10, 20, 30)
l = [40, 50, 60]
combined = list(t) + l
print("Combined List:", combined)

#Create a tuple of 4 numbers. Print the first and second elements separately.
tup = (2,1,5,7)
print(tup[0])
print(tup[1])

#Create a tuple with only one element. Print it and its type.
tup=(1,)
print(tup)
print(type(tup))

#Create a tuple of 4 numbers. Print the tuple and its type
tup=(1,2,3,4)
print(tup)
print(type(tup))

#Create a tuple of 4 numbers. Print elements from index 1 to 2 using slicing.
tup=(1,2,3,4)
print(tup[1:3])

#Create a tuple of 4 numbers. Find and print the index of value 2.
tup=(1,2,3,4)
print(tup.index(2))

#Create a tuple where 2 appears twice. Count and print how many times 2 appears
tup=(1,2,3,2,4)
print(tup.count(2))

#Write a programme to count the number of student with the "A" grade in the following tuple.
grade=("C","B","A","D","A","B","A")
print(grade.count("A"))

#Store the above values in a list & sort them from "A" to "D"
grade=["C","D","A","A","B","B","A"]
grade.sort()
print(grade)