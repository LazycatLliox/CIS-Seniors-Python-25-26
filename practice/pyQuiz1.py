'''
name: atreyu
'''

for i in range(6):
    print(i , end = " ")

for i in range(3,9):
    print(i, end = "\n")

for i in range(0, 12, +2):
    print(i, end = "\n\n")

for i in range(10, 0, -1):
    print(i, end = "\n\n")

for i in range(1, 10):
    print(i, 5 * i)

age = int(input("Please Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")

for number in range(1,11):
    if (number % 2) == 0:
        print("Even")
    else:
        print("Odd")

for i in range(20, -5, -5):
    print("Countdown: ",i, end = '\n')

for i in range(1,7):
    if i <= 3:
        print("Number", i, "is small\n")
    else:
        print("Number", i, "is large\n")

number = int(input("Please enter a number: "))

for i in range(1, (number +2), +2):
    if i <= 3:
        print("Low:", i)
    else:
        print("High:", i)

for i in range(15, -3, -3):
    if i >= 3:
        print(i, "\n")
    else:
        print("Blast off")