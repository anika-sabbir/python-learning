tup = (2,1,5,7)
print(tup[0])
print(tup[1])

#
tup=(1,)
print(tup)
print(type(tup))

#
tup=(1,2,3,4)
print(tup)
print(type(tup))

#
tup=(1,2,3,4)
print(tup[1:3])

#
tup=(1,2,3,4)
print(tup.index(2))

#
tup=(1,2,3,2,4)
print(tup.count(2))

#Write a programme to count the number of student with the "A" grade in the following tuple.
grade=("C","B","A","D","A","B","A")
print(grade.count("A"))

#Store the above values in a list & sort them from "A" to "D"
grade=["C","D","A","A","B","B","A"]
grade.sort()
print(grade)