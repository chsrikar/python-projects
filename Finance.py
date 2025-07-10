import pandas as pd

class FinanceTracker:
    def __init__(self):
        self.data = pd.DataFrame(columns=['Type', 'Amount', 'Category', 'Description'])

    def add_transaction(self, transaction_type, amount, category, description):
        new_transaction = pd.DataFrame({
            'Type': [transaction_type],
            'Amount': [amount],
            'Category': [category],
            'Description': [description]
        })
        
        # Only concatenate if new_transaction is not empty
        if not new_transaction.empty:
            self.data = pd.concat([self.data, new_transaction], ignore_index=True)

    def view_transactions(self):
        if self.data.empty:
            print("No transactions found.")
        else:
            print(self.data)

    def calculate_balance(self):
        income = self.data[self.data['Type'].str.lower() == 'income']['Amount'].sum()
        expenses = self.data[self.data['Type'].str.lower() == 'expense']['Amount'].sum()
        balance = income - expenses
        return balance

    def generate_report(self):
        balance = self.calculate_balance()
        print("\n--- Financial Report ---")
        print(f"Total Income: ${self.data[self.data['Type'].str.lower() == 'income']['Amount'].sum()}")
        print(f"Total Expenses: ${self.data[self.data['Type'].str.lower() == 'expense']['Amount'].sum()}")
        print(f"Current Balance: ${balance}\n")

def main():
    tracker = FinanceTracker()
    
    while True:
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Generate Report")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            transaction_type = input("Enter transaction type (Income/Expense): ").strip().capitalize()
            amount = float(input("Enter amount: "))
            category = input("Enter category: ").strip()
            description = input("Enter description: ").strip()
            tracker.add_transaction(transaction_type, amount, category, description)
            print("Transaction added successfully!\n")
        
        elif choice == '2':
            tracker.view_transactions()
        
        elif choice == '3':
            tracker.generate_report()
        
        elif choice == '4':
            print("Exiting the Finance Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
