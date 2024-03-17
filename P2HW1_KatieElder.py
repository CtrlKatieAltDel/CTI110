# Katie Elder
# Date: 03/17/2024
# Program: P2HW1
# Description: This program helps users manage their travel budget.

# Prompt the user to enter their budget 
budget = float(input("Enter your budget: "))

# Prompt the user to enter their travel destination 
destination = input("Enter your travel destination: ")

# Prompt the user to enter the amount they will spend on gas 
gas_expense = float(input("Amount you will spend on gas: "))

# Prompt the user to enter the amount they will spend on accommodation
accommodation_expense = float(input("Amount you will spend on accommodation: "))

# Prompt the user to enter the amount they will spend on food
food_expense = float(input("Amount you will spend on food: "))

# Calculate the total expenses by adding gas, accommodation, and food expenses
total_expenses = round(gas_expense + accommodation_expense + food_expense, 2)

# Calculate the remaining budget by subtracting total expenses from the initial budget
remaining_budget = round(budget - total_expenses, 2)

# Print the travel destination, total expenses, and the remaining budget
print(f"\nTravel Destination: {destination}")
print(f"{'Total Expenses:':<20} ${total_expenses:,.2f}")
print(f"{'Remaining Budget:':<20} ${remaining_budget:,.2f}")