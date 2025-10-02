''' 
Name: Atreyu 
Date: 10/2/25
Class: CIS sienors 25-26


set the sum to 0.0 
input a string 
while the is not the empty string 
    convert string to float 
    add float to sum 
    input a string 
print sum

loop control variable - the first input statment that inzilizes a variable to a value that the loop condition can test
'''

theSum = 0
data = input("Enter a number or just enter to quit:")

while data != "":
    number = float(data)
    theSum += number 
    data = input("Enter a number or just enter to quit:")

print("The sum is", theSum)

print("\n\nA Count-Controlled While loop")

#sumation with a for loop
theSum = 0
for count in range(1, 10001):
    theSum += count
print(theSum, "\n\n")

#sumation with while loop 
theSum = 0 
count = 1 

while count <= 10000:
    theSum += count
    count += 1 # control variable incriment
print(theSum)

print("\n\nCounting down with loops")

for count in range(10, 0, -1):
    print(count, end= " ")
    

count = 10 

while count >= 1:
    print(count, end = " ")
    count -= 1

print("\n\nThe while true statment with break statment")

theSum = 0.0 

while True:
    data = input("Enter a number or hit enter to quit:")
    if data == "":
        break
    number = float(data)
    theSum += number

print("The sum is" , theSum)

print("\n\nGrading Example")
while True:
    number = int(input("Enter numeric grade"))
    if number >= 0 and number <= 100:
        break
    else:
        print("Please enter a number 0-100")
print(number)

print("\n\n Diffrent Grading example\n")
done = False
while not done:
    number = int(input("Enter a numeric grade"))
    if number >+ 0 and number <= 100:
        done = True
    else:
        print("Please Enter a number 1- 100")
print(number)
