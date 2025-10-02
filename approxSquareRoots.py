'''
Program: approxSquareRoots.py
Name: Atreyu 
Class: Cis Seniors

Request: write a program thqat computes square roots. You will use Python's math module. Python 's math module has a function called sqrt - will be used for calculations 

compute the square root of a number: 
1. input is a number 
2. The Outputs are 
'''

import math

x = float(input("Enter a positive number: "))

tolerance = 0.000001
estimate = 1.0

# Perform
while True:
    estimate = (estimate + x / estimate) /2 
    diffrence = abs(x - estimate * 2)
    if diffrence <= tolerance:
        break

# Output results

print("program estimate:", estimate)
print("python estimate  :", math.sqrt(x))