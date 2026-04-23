#/Print "hello" 5 times using a while loop (with a count variable).

count = 1
while count <= 5 :
    print("hello")
    count += 1

print(count)


#/Print numbers from 1 to 5 using a while loop.

i = 1
while i <= 5:
    print(i)
    i+=1

#/Print numbers from 5 down to 1 (countdown) using a while loop.
i =5
while i>=1:
   print(i)
   i-=1

print("loop ended")

#/Print numbers from 1 to 100.

i=1
while i<=100:
    print(i)
    i+=1

#/print numbers from 100 to 1.
i=100
while i>=1:
    print(i)
    i-=1

#/Print the multiplication table of a number n.
n = int(input("enter number:"))
i=1
while i<=10:
    print(n*i)
    i+=1

#/Print the elements of the following list using a loop:(1,4,9,16,25,36,49,64,81,100).
nums =[1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx <len(nums):
    print(idx)
    idx +=1

#/Search for a number x in this tuple using loop:(1,4,9,16,25,36,49,64,81,100).
nums =(1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i<len(nums):
    if(nums[i]==x):
        print("found at idx",i)
    i +=1


#/Print 1 to 5 using while loop, stop at 3.
i = 1
while i<= 5:
    print(i)
    if(i == 3):
        break
    i+=1
print("end of loop")


#/Find number 36 in a tuple using while loop.
nums =(1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i<len(nums):
    if(nums[i]==x):
        print("found at idx",i)
        break
    else:
        print("finding..")
    i +=1
print("end of loop")

#/Print 0 to 5 but skip 3.
i = 0
while i<= 5 :
    if(i == 3):
        i+=1
        continue 
    print(i)
    i+=1

#/Print only odd numbers 1 to 10.
i = 1
while i<= 10 :
    if(i%2 == 0):
        i+=1
        continue 
    print(i)
    i+=1

#/Print only even numbers 1 to 10.
i = 1
while i<= 10 :
    if(i%2 != 0):
        i+= 1
        continue 
    print(i)
    i+=1

#/Print all elements of list [1,2,3,4,5] using for loop.
nums = [1,2,3,4,5]

for val in nums:
    print(val)

#/Print all elements of tuple (1,2,3,45) using for loop.
tup =(1,2,3,45,)

for num in tup:
    print(num)

#/Print each character of "anika" using for loop.
str = "anika"

for char in str:
    print(char)


#/Loop through "anika", print "i found" when you see 'i', then stop.
str = "anika"

for char in str:
    if char == 'i':
        print("i found")
        break
    print(char)
else:
    print("END")

#Print the elements of the following list using a loop:(1,4,9,16,25,36,49,64,81,100)
nums =[1,4,9,16,25,36,49,64,81,100]

for el in nums:
    print(el)

#/#Print for a number x in this tuple using a loop:(1,4,9,16,25,36,49,64,81,100)
nums =[1,4,9,16,25,36,49,64,81,100]
x= 49
for el in nums:
    if(el == x):
        print("number found at idx",idx)
        idx+=1

#/Print elements of range(5) by index.
seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])

#/Print all of range(5) using for loop.
seq = range(5)
for i in seq:
    print(i)

#/Print numbers 2 to 8 with step 2 using range.
for i in range(2,9,2):
    print(i)

#/using for range:- print number from 1 to 100.
for i in range(1,101):
    print(i)

#/using for range:- print number from 100 to 1.
for i in range(100,0,-1):
    print(i)

#/print the multiplication table of a number n.
n = int(input("enter num:"))

for i in range(1,11):
    print(n*i)

#/pass statement
for i in range(5):
      pass
print("some useful work")

#/WAP to find the sum of first n numbers.
n=5
sum = 0
for i in range(1,n+1):
    sum+=i
    print("total sum=",sum)

#/WAP to find the sum of first n numbers.(using while)
n =8
sum =0
i=1
while i<=n:
    sum+= i
    i+= 1
    print("total sum=",sum)

#/WAP to find the factorial of first n numbers.(using for)
n=5
fact=1
for i in range(1,n+1):
    fact *=i
    print("factorial=",fact)