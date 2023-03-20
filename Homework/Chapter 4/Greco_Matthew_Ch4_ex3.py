#create budget comparing program
#ask user for budget value
#create while loop that prompts for input of expense
#decrement total budged value by user provided input
#prompt user if there is another expense
#after loop, print value of budget

#initialize user_budget variable to user input float value
user_budget = float(input("Enter your monthly budget: $"))

#initialize choice variable to 'y' for while loop conditional
choice = 'y'

#define while loop conditional
while choice == 'y':
    #initialize expense variable to user input cast as float
    expense = float(input("Enter the cost of this expense: $"))

    #decrement budget by expense value
    user_budget -= expense

    #prompt user if more inputs are required, assign input to choice for while loop comparison
    choice = input("Do you have another expense to input? (y/n): ")

#if budget is positive
if (user_budget >= 0):
    #print value remaining formatted
    print(f"Your remaining budget is ${user_budget:,.2f}")
else:
    #assign absolute value of user_budget to modified_budget variable
    modified_budget = user_budget * -1
    #print modified budget formatted
    print(f"You are over budget by ${modified_budget:,.2f}")