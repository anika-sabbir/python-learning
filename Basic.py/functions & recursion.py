#/ Write a function, calc_sum(a,b) — print and return the sum. Call with (5,10) and (26,31).

def calc_sum(a,b):
   sum = a + b
   print(sum)
   return sum

calc_sum(5,10)

calc_sum(26,31)

#/ write a function to calc_sum in one line using only return.
def calc_sum(a,b): 
   return a+b 
sum = calc_sum(120,220) 
print(sum)

#/Write a function to print_hello() — no parameters, just prints "hello". Call it twice.
def print_hello():
   print("hello")

print_hello()
print_hello()

#/ Write a function to calc_avg(a,b,c) — print and return the average. Call with (65,30,33).
def calc_avg(a,b,c):
   sum = a+b+c
   avg =sum/3
   print(avg)
   return avg

calc_avg(65,30,33)

#/Write  a function to print the length of a list.(list is  the parameter)
cities =["Chattogram","Dhaka","Sylhet"]

def print_len(list):
   print(len(list))
print_len(cities)

#WAF to print the elements of a list in a single line.(list is the parameter)
cities =["Chattogram","Dhaka","Sylhet"]
print(cities[0],end=" ")
print(cities[1],end=" ")
def print_len(list):
   print(len(list))
print_len(cities)

#
cities =["Chattogram","Dhaka","Sylhet"]

def print_len(list):
   print(len(list))

def print_list(list):
   for item in list:
      print(item,end=" ")
print()
print_list(cities)

#/write a function to find the factorial of n.(n is the parameter)
def cal_fact(n):
   fact = 1
   for i in range(1, n+1):
      fact*=i
      print(fact)

cal_fact(6)

#/WAF to convert USD to TK
def converter(usd_val):
    tk_val = usd_val * 125   # example conversion rate
    print(usd_val, "USD =", tk_val, "TK")

converter(2)





#/Write a recursive function that prints numbers from n down to 1.
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(5) 


#/Write a recursive function to calculate the factorial of a number. Call it with n
def fact(n):
   if(n == 1 or n == 0):
      return 1
   return fact(n-1) * n

print(fact(6))

#/Write a recursive function to calculate the sum of first n natural numbers.
def calc_sum(n):
   if(n == 0):
      return 0
   return calc_sum(n-1) + n
sum = calc_sum(10)
print(sum)


#/Write a recursive function to print all elements in list.
def print_list(list,idx=0):
   if(idx == len(list)):
      return
   print(list[idx])
   print_list(list,idx+1)
fruits =["mango","banana","apple"]
print_list(fruits)