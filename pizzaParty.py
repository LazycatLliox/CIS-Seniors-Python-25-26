'''
Program: pizzaParty.py
Author: Atreyu Blum
Date: 10/16/2025
'''


import math

# Friday Night Pizza Party

# Constants
SLICES = 8
TAX_RATE = 0.07  # 7% tax
DELIVER_FEE = 0.2

weekendTotal = 0
#INPUTS
numPeople = int(input("Enter the number of people: "))
avgSlices = float(input("Enter the average number of slices per person: "))
pizzaCost = float(input("Enter the cost of the pizza: "))

# calculate cost 
pizzas = (avgSlices * numPeople) / SLICES
num_pizzas = math.ceil(pizzas)
pizzaCost = num_pizzas * pizzaCost
tax = pizzaCost * TAX_RATE
dilivery = (pizzaCost + tax) * DELIVER_FEE
total = pizzaCost + tax + dilivery
weekendTotal += total

# output bill
print("\nFriday Night Pizza Party")
print(f"{num_pizzas} Pizzas : $ {pizzaCost:.2f}")
print(f"Tax : $ {tax:.2f}")
print(f"Delivery Fee : $ {dilivery:.2f}")
print(f"Total Bill : $ {total:.2f}")

# Saturday Night Pizza Party

# Constants
SLICES = 8
TAX_RATE = 0.07  # 7% tax
DELIVER_FEE = 0.2

weekendTotal = 0
#INPUTS
numPeople = int(input("Enter the number of people: "))
avgSlices = float(input("Enter the average number of slices per person: "))
pizzaCost = float(input("Enter the cost of the pizza: "))

# calculate cost 
pizzas = (avgSlices * numPeople) / SLICES
num_pizzas = math.ceil(pizzas)
pizzaCost = num_pizzas * pizzaCost
tax = pizzaCost * TAX_RATE
dilivery = (pizzaCost + tax) * DELIVER_FEE
total = pizzaCost + tax + dilivery
weekendTotal += total

# output bill
print("\nSaturday Night Pizza Party")
print(f"{num_pizzas} Pizzas : $ {pizzaCost:.2f}")
print(f"Tax : $ {tax:.2f}")
print(f"Delivery Fee : $ {dilivery:.2f}")
print(f"Total Bill : $ {total:.2f}")

# Sunday Night Pizza Party

# Constants
SLICES = 8
TAX_RATE = 0.07  # 7% tax
DELIVER_FEE = 0.2

weekendTotal = 0
#INPUTS
numPeople = int(input("Enter the number of people: "))
avgSlices = float(input("Enter the average number of slices per person: "))
pizzaCost = float(input("Enter the cost of the pizza: "))

# calculate cost 
pizzas = (avgSlices * numPeople) / SLICES
num_pizzas = math.ceil(pizzas)
pizzaCost = num_pizzas * pizzaCost
tax = pizzaCost * TAX_RATE
dilivery = (pizzaCost + tax) * DELIVER_FEE
total = pizzaCost + tax + dilivery
weekendTotal += total

# output bill
print("\nSunday Night Pizza Party")
print(f"{num_pizzas} Pizzas : $ {pizzaCost:.2f}")
print(f"Tax : $ {tax:.2f}")
print(f"Delivery Fee : $ {dilivery:.2f}")
print(f"Total Bill : $ {total:.2f}")

# output weekend total
print(f"\nWeekend Total : $ {weekendTotal:.2f}")

