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