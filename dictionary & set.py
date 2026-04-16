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