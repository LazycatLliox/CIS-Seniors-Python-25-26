'''
filename: quizScorer.py
Name: Atreyu Blum
Course Name: CIS Seinors 25-26
Date: 9/25/2025
'''
# inputs 
studentName = input("Enter your name: ")

test = int(input("How many questions are there (5-10): "))

totalCorrect = 0
for question in range(int(test)):
    anwser = int(input("Question " + str(question + 1) + ": "))
    if anwser == 1:
        print("correct")
        totalCorrect += 1
    elif anwser == 0:
        print("Incorrect")
    else:
        print("Invalid input")
    

score = (totalCorrect / int(test) * 100)

print(studentName , "You got" , totalCorrect , "out of" , test , "question correct")

print("Your score is" , float(score) , "%")

if score >= 70: 
    print("You Passed")
else:
    print("you failed")
