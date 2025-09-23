'''
filename: fitnessTracker.py
Name: Atreyu Blum
Course Name: CIS Seniors 25-26
Date: 9/23/2025
'''

# Fitness Tracker inputs 
userName = input("Enter your username: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (in pounds): "))
height = float(input("Enter your height (in inches): "))
weeklyExerciseHours = float(input("Enter your average weekly exercise hours: "))
FitnessGoal = input("Enter your fitness goal: ")

# Calculations
BMI = (weight / (height * height)) * 703
WeeklyExerciseMinutes = weeklyExerciseHours * 60
weeklyCalories = weeklyExerciseHours * 300

# Print Fitness Tracker Information

print("\nFitness Tracker Profile\n\n")

print("Personal Information:\n")

print("Username:", userName)
print("Age:", age)
print("Weight (lbs):", weight)
print("Height (in):", height)

print("\n\nFitness Metrics:\n")
print("BMI:" ,BMI)
print("Weekly Exercise (hours):", weeklyExerciseHours)
print("Weekly Exercise (minutes):", WeeklyExerciseMinutes)
print("Estimated Weekly Calories Burned:", weeklyCalories)

print("\nFitness Goal:", FitnessGoal)

print("\nKeep pushing towards your goal, ", userName, "!")
