'''
Porject Name: Grade Report Generator
Author: Atreyu Blum
Date: 11/6/25
'''


# Challenge: Complete Grade Book System
student1 = {
    "name": "Bob",
    "id": "S122",
    "math": 88,
    "english": 92,
    "science": 79,
    "history": 85,
    "average": 86

}
student2 = {
    "name": "Alice",
    "id": "S123",
    "math": 95,
    "english": 89,
    "science": 92,
    "history": 90,
    "average": 91.5
}
student3 = {
    "name": "Eve",
    "id": "S124",
    "math": 76,
    "english": 85,
    "science": 80,
    "history": 78,
    "average": 79.75
}

# Create a list of student dictionaries
grade_book = [
    student1,
    student2,
    student3,
]

def print_class_report(students):
    """Prints a formatted report for all students"""
    # Your code here
    for student in students:
        print(f"Student Name: {student['name']}")
        print(f"Student ID: {student['id']}")
        print(f"Math: {student['math']}")
        print(f"English: {student['english']}") 
        print(f"Science: {student['science']}")
        print(f"History: {student['history']}")
        print(f"Average: {student['average']:.2f}%")
        print("-" * 30)
              
    pass

def find_top_student(students):
    """Returns the student with the highest average"""
    # Your code here
    print("Top student")
    print("-" * 30)

    highest_avg = 1
    top_student = None
    for student in students:
        if student["average"] > highest_avg:
            top_student = student
            
    


    pass

def count_honor_students(students):
    """Counts students with average >= 90"""
    # Your code here
    pass

# Test your functions
print_class_report(grade_book)
top_student = find_top_student(grade_book)
honor_count = count_honor_students(grade_book)