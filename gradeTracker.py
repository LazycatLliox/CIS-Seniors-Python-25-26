'''
file: grade tracker
Name: Atreyu 
course: seinors python 25-26
date: 10/1/25
'''
print("=" * 40)
print("Welcome to the grade tracker")
print("=" * 40)



while True: 
    students = input('How many sudents do you have (input a number 1- 20): ')
    if students.isdigit():
        students = int(students)
        if students >= 1 and students <= 20: 
            break
        else:
            print('please enter a number 1-20')
        
    else:
        print('invalide input')

studentCount =[]
totalPoints = 0
highScore = None 
lowestScore = None 
passCount = 0

grade_A = 0
grade_B = 0
grade_C = 0
grade_D = 0 
grade_F = 0

for i in range(students):
    print('/n student' , str(i + 1) )
    name = input("Enter student name: ")
    while True:
        score_Input = input('Enter test score: ')
        try: 
            score = float(score_Input)
            if score >= 0 and score <= 100:
                break
            else:
                print('Please enter a number 1-100')
        except:
            print('Invalid Input')
    
    #Assign Letter Grade
    if score >= 90:
        letter = "A"
        grade_A += 1
    elif score >= 80:
        letter = "B"
        grade_B += 1
    elif score >= 70:
        letter = "C"
        grade_C += 1
    elif score >= 60:
        letter = "D"
        grade_D += 1
    else:
        letter = "F"
        grade_F += 1
    
    studentCount.append([name , score, letter])

    totalPoints += score 
    if highScore is None or score > highScore:
        highScore = score
    if lowestScore is None or score < lowestScore:
        lowestScore = score 
    if score >= 70:
        passCount += 1 
    
    avarageScore = totalPoints / students

    


