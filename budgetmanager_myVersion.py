overall_budget = 2500
budgeting = {} 
spending = {}

def add_budget(item, amount):
    budgeting[item] = amount
    global overall_budget 
    overall_budget -= amount

def spend(item, spend):
    spending[item] = spending.get(item, 0) + spend

def print_summary():
    tBudgeted = 0
    tSpent = 0
    tRemaining = 0
    print(f"{'Item':<15}{"Budgeted":>14}{"Spent":>15}{"Remaining":>15} \n{"--------------":<15}{"--------------":<15}{"--------------":<15}{"--------------":<15}")
    for item in budgeting:
        spent_amount = spending.get(item, 0)
        tBudgeted += budgeting[item]
        tSpent += spent_amount
        tRemaining += (budgeting[item]-spent_amount)
        print(f"{item:<15}{budgeting[item]:>14}{spent_amount:>15}{budgeting[item]-spent_amount:>15}")
    print(f"{"--------------":<15}{"--------------":<15}{"--------------":<15}{"--------------":<15}")
    print(f"{"Total":<15}{tBudgeted:>14}{tSpent:>15}{tRemaining:>15}")

add_budget("Groceries", 500)
add_budget("Rent", 900)
spend("Groceries", 35)
spend("Groceries", 15)
print_summary()