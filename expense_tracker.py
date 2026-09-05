expenses = []

print("===== Personal Expense Tracker =====")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")

            expense = {
                "amount": amount,
                "category": category
            }

            expenses.append(expense)

            print("Expense added successfully!")

        except ValueError:
            print("Invalid amount. Please enter a number.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\n----- Expenses -----")
            for expense in expenses:
                print("Category:", expense["category"])
                print("Amount:", expense["amount"])

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Total Expenditure:", total)

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")