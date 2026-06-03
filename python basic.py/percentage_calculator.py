#Feature 1: X of a number
percentage =float(input("Enter percentage num:"))
number =float(input("Enter number:"))
result =(percentage /100 )* number
print("Answer:", result)

#Feature 2: Discount
price =float(input("Enter original price:"))
discount =float(input("Enter discount %:"))
saved =(discount / 100) * price
final_price = price - saved
print("You save:", saved)
print("You pay:", final_price)

#Feature 3: What % is X of Y?
part =float(input("Enter part:"))
whole =float(input("Enter whole :"))
result2 = (part / whole)* 100
print("Answer:", result2, "%")