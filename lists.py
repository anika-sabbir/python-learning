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



