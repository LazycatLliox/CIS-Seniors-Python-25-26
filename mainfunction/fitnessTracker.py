# UNSTRUCTURED PROGRAM - Needs fixing!
# print("Fitness Tracker")
# print("===============")

# exercise = input("What exercise did you do? ")
# duration_str = input("How many minutes? ")
# duration = int(duration_str)

# calories_per_minute = 8  # Average
# total_calories = duration * calories_per_minute

# print("Exercise: " + exercise)
# print("Duration: " + str(duration) + " minutes")
# print("Calories burned: " + str(total_calories))

# if total_calories >= 300:
#     print("Great workout!")
# else:
#     print("Good start! Try for 30+ minutes next time.")

def display_header():
    '''
    displays program header and welcome message 

    has no parameters and no returns just for display
    '''

    print("=" * 30)
    print("\n=== Fitness Tracker ===\n")
    print("Displaying your fitness journey!\n")
    print("=" * 30)


def exercise_info():
    print("Enter the exercise details:")
    exercise = input("What exercise did you do? ")
    duration = int(input("How many minutes did you exercise? "))
    return exercise, duration

def calculate_calories(duration):
    calories_per_minute = 8  
    total_calories = duration * calories_per_minute
    return total_calories

def summary_report(exercise, duration, total_calories):
    print("\n=== Exercise Summary ===")
    print(f"Exercise: {exercise}")
    print(f"Duration: {duration} minutes")
    print(f"Calories burned: {total_calories}")

    if total_calories >= 300:
        print("Great workout!")
    else:
        print("Good start! Try for 30+ minutes next time.")

def main():
    print("Fitness Tracker")
    print("===============")

    display_header()

    exercise, duration = exercise_info()

    total_calories = calculate_calories(duration)

    summary_report(exercise, duration, total_calories)



if __name__ == "__main__":
    main()



