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