#Normal String
str="I am Anika"
print(str)

#String with newline(\n)
str1="I am Anika\n I am an engineer"
print(str1)

#String with tab(\t)
str2="I am Anika\t I am an engineer"
print(str2)

# Length of string
str1="I am Anika\n I am an engineer"
len1=len(str1)
print(len1)
str2="I am Anika\t I am an engineer"
len2=len(str2)
print(len2)

#String concatenation
final_str=str1+ " "+str2
print(final_str)
print(len(final_str))

#index
str="Anika Sabbir" 
chr=str[2]
print(chr)

#String indxing -get single character by position
str="Anika Sabbir" 
print(str[3])

#Slicing -get single characters from index 0 to 4 (5 not included)
str="Anika Sabbir"
print(str[0:5])

# Slicing - same as [0:5], start is 0 by default
str="Anika Sabbir"
print(str[:5])

# Slicing - first part and second part
str="Anika Sabbir"
print(str[:5]) #[0:5]
print(str[5:]) #[5: len(str)]

#slicing(Negative Index)
str="Anika"
print(str[-5:-2])


# String function - endswith()
# checks if string ends with given word, returns True or False
str="I am an Engineer"
print(str.endswith("ineer"))

str="I am an Engineer"
print(str.endswith("eng"))

# capitalize() - makes first letter uppercase, rest lowercase
str="i am an Engineer"
print(str.capitalize())

str="i am an Engineer"
print(str.capitalize())
print(str)

# capitalize() - reassign to actually change the variable
str="i am an Engineer"
str=str.capitalize()
print(str)

# replace() - replaces all 'a' with 'e'
str="I am an Engineer"
print(str.replace("a","e"))

# find() - returns index position of first 'e' found
str="I am an Engineer"
print(str.find("e"))