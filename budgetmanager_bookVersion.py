class BudgetManager:
    def __init__(self, amount):
        self.available = amount
        self.budgets = {}
        self.expenditure = {}

    def add_budget(self, name, amount):
        global available
        if name in self.budgets:
            raise ValueError(f"Budget {name} exists")
        if amount > self.available:
            raise ValueError("Insufficient funds")
        self.budgets[name] = amount
        self.available -= amount
        self.expenditure[name] = 0
        return self.available

    def spend(self, name, amount):
        if name not in self.expenditure:
            raise ValueError("No such budget")
        self.expenditure[name] += amount

    def print_summary(self):
        print("Budget            Budgeted      Spent  Remaining")
        print("--------------- ---------- ---------- ----------")
        total_budgeted = 0
        total_spent = 0
        total_remaining = 0
        for name in self.budgets:
            budgeted = self.budgets[name]
            spent = self.expenditure[name]
            remaining = budgeted - spent
            print(f"{name:15s} {budgeted:10.2f} {spent:10.2f} {remaining:10.2f}")
            total_budgeted += budgeted
            total_remaining += remaining
            total_spent += spent
        print("--------------- ---------- ---------- ----------")
        print(f"{"Total":15s} {total_budgeted:10.2f} {total_spent:10.2f} {total_remaining:10.2f}")
