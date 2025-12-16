'''
Program: carpetSales.py
Author: Atreyu Blum
Date: 10/16/2025
'''

# Constants
TAX_RATE = 0.07  # 7% tax
WASTE_PCT = 1.2
LABOR_RATE = 0.75

totalSales = 0

# order 1 

# input per sq ft, room length, room width
price = float(input("Enter the price per square foot: "))
width = int(input("Enter the width of the room in feet: "))
length = int(input("Enter the length of the room in feet: "))

# Calcualte room square footage

sqFt = width * length

# Calculate carpet cist including waste 
carpet = (sqFt * WASTE_PCT) * price

# Calculate labor cost 

labor = sqFt * LABOR_RATE

# Calculate tax
tax = (carpet + labor) * TAX_RATE

# Calculate total cost
total = carpet + labor + tax

# Output results 

print("\nOrder One")
print(f"Square Footage:", sqFt , "sq ft")
print(f"Carpet Cost: $ {carpet:.2f}")
print(f"Labor Cost: $ {labor:.2f}")
print(f"Tax: $ {tax:.2f}")
print(f"Total Cost: $ {total:.2f}")
totalSales += total

# order 2 

# input 
print("\nFor order two enter the price per sq ft, room length, room width separated by space. Ex: 2.99 12 10")
price, width, length = input().split()
price = float(price)
width = int(width)
length = int(length)


# calculations 
sqFt = width * length 
carpet = (sqFt * WASTE_PCT) * price
labor = sqFt * LABOR_RATE
tax = (carpet + labor) * TAX_RATE
total = carpet + labor + tax

print("\nOrder Two")
print(f"Square Footage:", sqFt , "sq ft")
print(f"Carpet Cost: $ {carpet:.2f}")
print(f"Labor Cost: $ {labor:.2f}")
print(f"Tax: $ {tax:.2f}")
print(f"Total Cost: $ {total:.2f}")
totalSales += total

# Order 3 

# input 
print("\nFor order three enter the price per sq ft, room length, room width separated by space. Ex: 2.99 12 10")
price, width, length = input().split()
price = float(price)
width = int(width)
length = int(length)


# calculations 
sqFt = width * length 
carpet = (sqFt * WASTE_PCT) * price
labor = sqFt * LABOR_RATE
tax = (carpet + labor) * TAX_RATE
total = carpet + labor + tax

print("\nOrder Three")
print(f"Square Footage:", sqFt , "sq ft")
print(f"Carpet Cost: $ {carpet:.2f}")
print(f"Labor Cost: $ {labor:.2f}")
print(f"Tax: $ {tax:.2f}")
print(f"Total Cost: $ {total:.2f}")
totalSales += total

# Output total sales
print("\nTotal Sales for all orders: $", f"{totalSales:.2f}")

