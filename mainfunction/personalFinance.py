"""
Name: Atreyu Blum
Date: 11/18/2025
file: Personal Finance Tracker.py

This program demonstrates proper pyhton structure using main function and helper functions.
"""
def display_header():
    """
    displays program header and welcome message

    this program has no prameters and no returns just for display :3
    """
    print("=" * 30)
    print("\n=== Person Finance Tracker ===\n")
    print("=" * 30)


def get_user_name():
    '''
    gets user's name 

    returns: variable name (string)

    Note: use a sperate function for this to keep each function to a single task
    '''

    name = input("What is your name? ")
    return name

def get_income():
    '''
    gets user's monthly income 

    Returns: variable income (float) in dollars

    note we convert the input to a float to handle decimal values and use for mathmatical operations
    '''
    income = float(input("Enter your monthly income: $"))
    return income 

def get_expenses():
    '''
    collect all expense categories from the user 

    returns: 
    expenses_dict (dict): dictionary with all expense categories
    total_expenses (float): total of all expenses

    note: this function demonstrates collecting multiple related inputs and origanizing them in a dictionary for easy access later
    '''
    print("\n--- Expense Tracking ---")
    # dictionary to store all expenses
    expenses = {}

    # get each expense category
    print("Enter your rent/housing cost: $")
    expenses['Rent/Housing'] = float(input())

    print("Enter your food/groceries cost: $")
    expenses['Food/Groceries'] = float(input())

    print("Enter your transportation cost: $")
    expenses['Transportation'] = float(input())

    print("Enter your entertainment budget: $")
    expenses['Entertainment'] = float(input())

    print("Enter Your savings goal: $")
    expenses['Savings'] = float(input())

    print("Enter any misscellaneous expenses: $")
    expenses['Miscellaneous'] = float(input())

    # calculate total expenses
    total = sum(expenses.values())

    # return both the dictionary and total
    return expenses, total

def calculate_remaining(income, expenses):
    '''
    
    '''
def provide_feedback(remaining, income):
    pass

def display_summary(name, income, expenses_dict, total_expenses, remaining, feedback):
    pass

def main():
    """
    main function - coordinates the entire program
    
    notice how the main function reads like a story
    1. display header
    2. get user name
    3. get income
    4. get expenses
    5. calculate remaining money
    6. provide feedback
    7. display summary
    8, say goodbye

    each step is a function call, making the logic easy to follow
    """

    #display Welcome message
    display_header()
    print("Welcome let's track your personal finances!\n")

    # get user information
    user_name = get_user_name()
    monthly_income = get_income()

    # get expenses
    # note: this function will return two values (tuple unpacking)
    expense_catigories, total_expenses = get_expenses()
if __name__ == "__main__":
    main()