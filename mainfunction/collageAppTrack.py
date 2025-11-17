def display_welcome():
    # displays program header
    print("=== College Application Tracker ===")

def collageCount():
    # gets number of collages to apply to
    num_collages = input("Enter the number of colleges you plan to apply to: ")
    return int(num_collages)

def applicationCost(numCollages):
    # calculates total application cost
    cost_per_application = 50  # assuming each application costs $50
    total_cost = numCollages * cost_per_application
    return total_cost

def satScore():
    # gets user's SAT score
    score = input("Enter your SAT score: ")
    return int(score)

def analyze_sat(score):
    # analyzes SAT score and provides feedback
    if score >= 1400:
        return "Excellent score!"
    elif score >= 1200:
        return "Good score!"
    elif score >= 1000:
        return "Average score."
    else:
        return "Consider retaking the SAT to improve your chances."
    

def display_summary(numcollages, totalcost, sat_score, sat_feedback):
    # displays summary of application information
    print("\n=== Application Summary ===")
    print(f"Number of Colleges to Apply To: {numcollages}")
    print(f"Total Application Cost: ${totalcost}")
    print(f"SAT Score: {sat_score}")
    print(f"Feedback: {sat_feedback}")

def main():
    print("Welcome to College Application Tracker")
    display_welcome()

    #college information
    numCollages = collageCount()
    totalCost = applicationCost(numCollages)
    sat = satScore()

    # analyze data
    feedback = analyze_sat(sat)

    # display results
    display_summary(numCollages, totalCost, sat, feedback)

    print("\n Good luck with your applications!")


if __name__ == "__main__":
    main()