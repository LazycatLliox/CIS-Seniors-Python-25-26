'''
file: taxForm.py
Name: Atreyu Blum
Date: 9/22/2025
Course: CIS Seniors 25-26

compute a person's income tax 
1. Significant Constants 
   tax rate 
   standard deduction
   deduction per dependent
2. Inputs 
    gross income
    number of dependents
3. Computations
    taxable income = gross income - standard deduction - deduction per dependent 

    income tax = is a fixed percentage of the taxable income
4. Outputs
    income tax
'''

print("\n\n My Tax Rate Calculator")
print("=" * 40)
# Intialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEDUCTION_PER_DEPENDENT = 3000.0

# Get the inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - (DEDUCTION_PER_DEPENDENT * numDependents)

incomeTax = taxableIncome * TAX_RATE

# Output the results
print("The income tax is: $" +str(incomeTax) + "\n\n")


