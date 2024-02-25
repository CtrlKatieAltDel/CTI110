# Katie Elder
# 2/25/2024
# P1HW12 
# This assignment is to help users in managing their travel budget.
# 3
budget = float(input("Enter your budget: "))

# 4
destination = input("Enter your travel destination: ")

# 5
gas_expense = float(input("Amount you will spend on gas: "))

# 6
accommodation_expense = float(input("Amount you will spend on accommodation: "))

# 7
food_expense = float(input("Amount you will spend on food: "))

# 8
total_expenses = gas_expense + accommodation_expense + food_expense

# 9
remaining_budget = budget - total_expenses

# 10
print(f"\nTravel Destination: {destination}")
print(f"Total Expenses: ${total_expenses}")
print(f"Remaining Budget: ${remaining_budget}")

