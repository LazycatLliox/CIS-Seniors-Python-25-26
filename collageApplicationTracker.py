'''
FileName: collageApplicationTracker.py
Name: Atreyu Blum
Date: 10/24/2025
'''

# Import statements
import math
# Constants (ALL_CAPS naming convention)
APPLICATION_FEE = 75.00
AVG_ACCEPTANCE_RATE = 55.0
MAX_IDEAL_DISTANCE = 500
# Welcome message
print("=" * 50)
# Your welcome code here
# Variables for student info
# Your code here
student_name = input("Enter your name: ")

# Lists to store college data
# Your code here
college_names = [input("Enter the name of college 1: "), input("Enter the name of college 2: "), input("Enter the name of college 3: ")]
collage_locations = [input("Enter the location of college 1: "), input("Enter the location of college 2: "), input("Enter the location of college 3: ")]
tution_costs = [float(input("Enter the tuition cost for college 1: ")), float(input("Enter the tuition cost for college 2: ")), float(input("Enter the tuition cost for college 3: "))]
distance_from_home = [float(input("Enter the distance from home for college 1 (in miles): ")), float(input("Enter the distance from home for college 2 (in miles): ")), float(input("Enter the distance from home for college 3 (in miles): "))]
acceptance_rate = [float(input("Enter the acceptance rate for college 1 (in %): ")), float(input("Enter the acceptance rate for college 2 (in %): ")), float(input("Enter the acceptance rate for college 3 (in %): "))]

# Calculations using Math module
# Your code here
totalTuitionCost = tution_costs[0] * 4 
totalTuitionCost = tution_costs[1] * 4 
totalTuitionCost = tution_costs[2] * 4 




# Summary report with f-strings
# Your code here

print(f"\nSummary Report for {student_name}")
print("-" * 50)
print(f"College 1: {college_names[0]}")
print(f"Location: {collage_locations[0]}")
print(f"Tuition Cost (per year): ${tution_costs[0]:.2f}")
print(f"Distance from Home: {distance_from_home[0]} miles")
print(f"Acceptance Rate: {acceptance_rate[0]}%")
print(f"Total Tuition Cost (4 years): ${totalTuitionCost:.2f}")
print("-" * 50)

print(f"College 2: {college_names[1]}")
print(f"Location: {collage_locations[1]}")
print(f"Tuition Cost (per year): ${tution_costs[1]:.2f}")
print(f"Distance from Home: {distance_from_home[1]} miles")
print(f"Acceptance Rate: {acceptance_rate[1]}%")
print(f"Total Tuition Cost (4 years): ${totalTuitionCost:.2f}")
print("-" * 50)

print(f"College 3: {college_names[2]}")
print(f"Location: {collage_locations[2]}")
print(f"Tuition Cost (per year): ${tution_costs[2]:.2f}")
print(f"Distance from Home: {distance_from_home[2]} miles")
print(f"Acceptance Rate: {acceptance_rate[2]}%")
print(f"Total Tuition Cost (4 years): ${totalTuitionCost:.2f}")
print("-" * 50)

print(f"Finacial Information:")
print(f"Total application fees for 3 colleges: ${APPLICATION_FEE * 3:.2f}")
print(f"Average annual tuition cost: ${(tution_costs[0] + tution_costs[1] + tution_costs[2]) / 3:.2f}")
print(f"Total 4-year tuition cost for all colleges: ${(tution_costs[0] + tution_costs[1] + tution_costs[2]) * 4:.2f}")

print(f"Most affordable college: {college_names[tution_costs.index(min(tution_costs))]} with tuition ${min(tution_costs):.2f} per year")
print(f"Most expensive college: {college_names[tution_costs.index(max(tution_costs))]} with tuition ${max(tution_costs):.2f} per year")
price_range = max(tution_costs) - min(tution_costs)
print(f"Price range between most and least expensive colleges: ${price_range:.2f}")

print("=" * 50)
print(f"Distance Traveled Information:")
print("=" * 50)

print(f"Average distance from home: {sum(distance_from_home) / len(distance_from_home):.2f} miles")
print(f"Total Distance if visiting all colleges: {sum(distance_from_home) * 2:.2f} miles (round trip)")
print(f"Estemated fule needed for visiting all colleges: {((sum(distance_from_home) * 2) / 25):.2f} gallons (assuming 25 mpg)")
print(f"Estimated cost of fuel for visiting all colleges: ${((sum(distance_from_home) * 2) / 25) * 3.50:.2f} (assuming $3.50 per gallon)")

print("=" * 50)
print(f"Acceptance Rate Information:")
print("=" * 50)
print(f"Your average acceptance rate across all colleges: {sum(acceptance_rate) / len(acceptance_rate):.2f}%")
print(f"National average acceptance rate: {AVG_ACCEPTANCE_RATE}%")
print(f"Your Application Ballance is:")
safe_colleges = [college_names[i] for i in range(len(acceptance_rate)) if acceptance_rate[i] > AVG_ACCEPTANCE_RATE]
match_colleges = [college_names[i] for i in range(len(acceptance_rate)) if acceptance_rate[i] == AVG_ACCEPTANCE_RATE]
reach_colleges = [college_names[i] for i in range(len(acceptance_rate)) if acceptance_rate[i] < AVG_ACCEPTANCE_RATE]

print(f"Thank you for using the College Application Tracker!")