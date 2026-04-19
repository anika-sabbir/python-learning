#/Create & print a basic dictionary (info with name, age, marks etc.)

info = {
    "key": "value",
    "name" : "anika",
    "learning" : "coding",
    "age" : 24,
    "is_adult": True,
    "marks": 95.5
    }
print(info)
#/Check the type of a dictionary using type()

info = {
    "name" : "anika",
    "subjects" : ["python","java"],
    "topics":("dict","set"),
    "age" : 24,
    "is_adult": True,
    "marks": 95.5
    }
print(type(info))

#/Access values using keys — info["name"], info["subjects"], info["topics"]

info = {
    "name" : "anika",
    "subjects" : ["python","java"],
    "topics":("dict","set"),
    "age" : 24,
    "is_adult": True,
    "marks": 95.5
    }
print(info["name"])
print(info["subjects"])
print(info["topics"])

#/Update & add keys — change "name" and add new key "surname"

info = {
    "name" : "anika",
    "subjects" : ["python","java"],
    "topics":("dict","set"),
    "age" : 24,
    "is_adult": True,
    "marks": 95.5
    }
info["name"]="anikasabbir"
info["surname"]="sabbir"
print(info)


#/Nested dictionary — access inner value like student["subjects"]["chem"]

student ={
    "name":"anika sabbir",
    "subjects":{
        "phy":98,
        "chem":95,
        "math":93
    }
}
#nested dictionary
print(student["subjects"]["chem"])


#/Print total number of keys using keys() method.


student ={
    "name":"anika sabbir",
    "subjects":{
        "phy":98,
        "chem":95,
        "math":93
    }
}
print(len(list(student.keys())))


#/Print all values using values() method.


student ={
    "name":"anika sabbir",
    "subjects":{
        "phy":98,
        "chem":95,
        "math":93
    }
}
print(student.values())

#/ Print all key-value pairs using items() method.


student ={
    "name":"anika sabbir",
    "subjects":{
        "phy":98,
        "chem":95,
        "math":93
    }
}
print(student.items())


#/ Store items() in a list and print first element.


student ={
    "name":"anika sabbir",
    "subjects":{
        "phy":98,
        "chem":95,
        "math":93
    }
}
pairs = list(student.items())
print(pairs[0])


#/Print name value using bracket notation and get() method.


student ={
    "name":"anika sabbir",
    "subjects":{
        "phy":98,
        "chem":95,
        "math":93
    }
}

print(student["name"])
print(student.get("name"))


#/Print name value using update() method.


student ={
    "name":"anika sabbir",
    "subjects":{
        "phy":98,
        "chem":95,
        "math":93
    }
}

student.update({"city": "chattogram"})
print(student)


#/Create a set with values {1, 2, 3, 4} and print it along with its type.
collection ={1,2,3,4}
print(collection)
print(type(collection))


#/Create a set with mixed values {1, 2, 3, 4, "hello", "world", "world"}. Print the set and its length.
collection ={1,2,3,4,"hello","world","world"}
print(collection)
print(len(collection))

#/Create an empty set and print its type.
collection = set()

print(type(collection))

#/Create an empty set, add values 1, 2, 3 one by one, then print the set.
collection =set()
collection.add(1)
collection.add(2)
collection.add(3)

print(collection)


#/Create a set with values 1, 2, 3. Add them one by one, then remove 2 and print the set.

collection =set()
collection.add(1)
collection.add(2)
collection.add(3)

collection.remove(2)

print(collection)


#/Create a set, add values 1, 2, 3, then clear the set and print its length.

collection =set()
collection.add(1)
collection.add(2)
collection.add(3)

collection.clear()

print(len(collection))

#/Create a set {"hello", "anika"} and print a randomly popped element.

collection={"hello","anika"}

print(collection.pop())

#/Create two sets set1 = {1,2,3} and set2 = {2,3,4}. Print their union (set1 and set2 remain unchanged).
set1={1,2,3}
set2={2,3,4}

print(set1.union(set2))
print(set1)
print(set2)

#/Create two sets set1 = {1,2,3} and set2 = {2,3,4}. Print their intersection.


set1={1,2,3}
set2={2,3,4}

print(set1.intersection(set2))

#/Store following word meanings in a python dictionary:
#table:"a piece of furniture","list of facts & figures"
#cat:"a samll animal"

info ={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts & figures"]

}
print(info)

#You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students?
#Given list:"python","java","c++","javascript","java","python","java","c++""c"

subjects={
    "python","java","c++","javascript","java","python","java","c++","c"
}

print(len(subjects))

#/WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. 
# Use subject name as key & marks as value.

marks ={}
x=int(input("enter phy :"))
marks.update({"phy":x})

x=int(input("enter math :"))
marks.update({"math":x})

x=int(input("enter chem :"))
marks.update({"chem":x})

print(marks)

#/Figure out a way to store 9 & 9.0 as separate values in the set.
#(You can take help of built-in data types)

values ={
    ("float",9.0),
    ("int",9)
}
print(values)