# Python Variable Name Validator
# Student Name: Atreyu Blum
# Date: 10/7/2025

# List of Python keywords
python_keywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
    'while', 'with', 'yield'
]

# Display welcome message
print("=== PYTHON VARIABLE NAME VALIDATOR ===")
print("This program checks if your variable name is valid in Python.")
print()

# Get user input
variable_name = input("Enter a variable name to validate: ")

# Your validation code goes here

if variable_name == "":
    print("Error Enter a variable name")
elif variable_name == python_keywords:
    print("Invalid variable name this is already a python keyword")

firstChar = variable_name[0]

if firstChar.isdigit():
    print("Invalid variable name cant start with a number")
else:
    print("Your Variable will work")
    
