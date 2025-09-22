'''
file: taxForm.py
Name: Atreyu Blum
Date: 9/22/2025
Course: CIS Seniors 25-26

Compute a Investment Report

1.The Inputs are 
    starting amount
    number of years
    interest rate

2. report is displayed in tabular format
3. computations and outputs
    for each year of the investment
        compute the intrest earned and add it to the investment amount print in a formatted row of results for that year
4. the ending investment amount you have paid in total are displayed
'''
print("\n\n My Investment Report")
print("=" * 40)
#inputs 

startingAmount = float(input("Enter the starting amount: "))
numberOfYears = int(input("Enter the number of years: "))
intrestRate = float(input("Enter the interest rate (as a decimal): "))

# show the report header
print("\n\nYear\tAmount on Deposit")
print("-" * 40)

# computations and outputs

totalAmount = startingAmount * (intrestRate) * numberOfYears

print(totalAmount)