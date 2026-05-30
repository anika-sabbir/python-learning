#You have a file data.txt with 5 lines. Read only the 3rd line using Python.
f= open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

#Write a program that counts how many lines are in a text file.
f= open("demo.txt","r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)

f.close()

#Copy the content of file1.txt into file2.txt using Python
f = open("demo.txt","w")

f.write("I want to learn JS tomorrow.")
f.close()
#Write a program that searches for a specific word in a file and prints the line number where it appears.
f = open("demo.txt","a")

f.write("Then I'll move to ReactJS.")
f.close()
#opens sample.txt with "w" mode but writes nothing.

f= open("sample.txt","w")
f.close()

#opens demo.txt with "r" mode but writes nothing.
with open("demo.txt","r")as f:
    data = f.read()
    print(data)

#remove delete file.
import os
os.remove("sample.txt")

#Create a new file"practice.txt"using python.Add the following data in it:
#Hi everyone
#we are learning File I/O
#using Java.
#I like programming in java.

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")

#Write a function that replaces all occurrences of "java" eith "python" in above file.
with open("practice.txt","r") as f:
    data =f.read()

    new_data = data.replace("Java","python")
    print(new_data)

    with open("practice.txt","w")as f:
        f.write(new_data)

#Search if the word "learning" exists in the file or not.
word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
      print("found")
    else:
        print("not found")

#WAF to find in which line of the file does the word "learning" occur first.
#Print -1 if word not found

def check_for_word():
  word = "xlearning"
with open("practice.txt","r") as f:
    data = f.read()
    if(word in data):
      print("found")
    else:
        print("not found")   
def check_for_line():
   word ="learning"
   data = True
   line_no =1
   with open("practice.txt","r") as f:
      while data:
         data = f.readline()
         if(word in data):
            print(line_no)
            return
            line_no +=1
      return -1

print(check_for_line())

# From a file containing numbers separated by comma,print te count of even numbers.

with open("practice.txt","r")as f:
   data = f.read()
   print(data)
      
   num =""
   for i in range(len(data)):
      if(data[i] == ","):
         print(int(num))
         num =""
      else:
         num +=data[i]

#Alternative Solution
count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)

  