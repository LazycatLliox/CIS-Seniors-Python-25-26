'''
File name: input.py
Name: Atreyu Blum
Course name: CIS Seniors 25-26
Date: 9/19/2025
'''

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
age = input("How old are you? ")
math = input("what is Pi?")
subject = input("Is this your favorite class? ")
print("Your name is "+ first_name + " " + last_name + ".")
print("You are " + age + " years old.")

if subject == "yes":
    subject = "true"
    print("I am happy to hear this is your favorite subject!")
else :
    subject = "false"
    print("You suck leave!")