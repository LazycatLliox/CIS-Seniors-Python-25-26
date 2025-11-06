
exam1_grade = float(input("Enter score on Exam 1 (out of 100): "))
exam2_grade = float(input("Enter score on Exam 2 (out of 100): "))
exam3_grade = float(input("Enter score on Exam 3 (out of 100): "))


examAvg = (exam1_grade + exam2_grade + exam3_grade) / 3

print(f"Your overall grade is: {examAvg:.2f}%")

print("\n\nStudent versions:")

# Calculates the overall grade for four equally weighted programming assignments, in which each assignment is graded out of 50 points. Hint: First calculate the percentage for each assignment (e.g., score / 50), then calculate the overall grade percentage (be sure to multiply the result by 100).
def calculate_grade(points):
    total_points = int(input("Enter the total number of points for this assignment: "))
    grade = (points / total_points)
    return grade

program1 = int(input("Enter the score you got on programing assignment 1: "))
program2 = int(input("Enter the score you got on programing assignment 2: "))
program3 = int(input("Enter the score you got on programing assignment 3: "))
program4 = int(input("Enter the score you got on programing assignment 4: "))

#calculate overall grade for programming assignments
grade1 = calculate_grade(program1) # call the function and pass arguments
grade2 = calculate_grade(program2)
grade3 = calculate_grade(program3)
grade4 = calculate_grade(program4)

progAvg = ((grade1 + grade2 + grade3 + grade4) / 4) * 100

print(f"\nStudent overall programming assignment grade is: {progAvg:.2f}%")
# Calculates the overall grade for four equally weighted programming assignments, in which assignments 1 and 2 are graded out of 50 points and assignments 3 and 4 are graded out of 75 points.
assign1 = int(input("Enter the score you got on programming assignment 1: "))
assign2 = int(input("Enter the score you got on programming assignment 2: "))
assign3 = int(input("Enter the score you got on programming assignment 3: "))
assign4 = int(input("Enter the score you got on programming assignment 4: "))

assignGrade1 = calculate_grade(assign1)
assignGrade2 = calculate_grade(assign2)
assignGrade3 = calculate_grade(assign3)
assignGrade4 = calculate_grade(assign4)

progAvg = ((assignGrade1 + assignGrade2 + assignGrade3 + assignGrade4) / 4) * 100

print(f"\nStudent overall programming assignment grade is: {progAvg:.2f}%")
# Calculates the overall grade for a course with three equally weighted exams (graded out of 100 points) that account for 60% of the overall grade and four equally weighted programming assignments (graded out of 50 points) that account for 40% of the overall grade. Hint: The overall grade can be calculated as 0.6 * averageExamScore + 0.4 * averageProgScore.
print("\n Section 3:")

overallAvg = (0.6 * examAvg) + (0.4 * progAvg)
print(f"\nStudent overall Average is: {overallAvg:.2f}%")

