'''
python has a module caled random. it needs to be imported 
'''

import random
for roll in range(6):
    print(random.randint(1,6), end = " ")


smaller = int(input("Enter the smaller number"))
larger = int(input("Enter the larger number"))
myNumber = random.randint(smaller, larger)
count = 0 

while True:
    count += 1 
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too small")
    elif userNumber > myNumber:
        print("Too Large")
    else:
        print("Congrats You've got in", count, "tries")
        break