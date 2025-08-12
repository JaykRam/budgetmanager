import budgetmanager_bookVersion
outgoings = budgetmanager_bookVersion.BudgetManager(2500)

outgoings.add_budget("Groceries", 500)
outgoings.print_summary()