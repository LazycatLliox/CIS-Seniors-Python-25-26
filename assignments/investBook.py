'''
file: investBook.py
Name: Atreyu Blum
Date: 9/23/2025
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
print("\n\n")
print("=" * 40)
print("Investment Report")
print("=" * 40)

# inputs
startBalance = float(input("Enter the starting balance: "))
numYears = int(input("Enter the number of years: "))
rate = int(input("Enter the interest rate (as a percent): "))

#covert the rate to a decimal
rate = rate / 100


# initialize the accumulator for total interest earned
totalInterest = 0.0


# Displat the header 

print("%4s%18s%10s%16s" % ("Year", "Starting Balance", "Interest Earned", "Ending Balance"))

#compute and display the results for each year

for year in range(1, numYears + 1):
    intrest = startBalance * rate 
    endBalence = startBalance + intrest
    totalInterest += intrest
    print("%4d%18.2f%10.2f%16.2f" % (numYears, startBalance, intrest, endBalence))
    startBalance = endBalence 


# display the totals for the period 

print("Ending Balence: $%0.2f" % endBalence)
print("Total Intrest: $%0.2f" % totalInterest)