from src.menu import show_menu
from src.file_manager import load_expenses, save_expenses
from src.expense import Expense
from src.reports import category_summary, monthly_report
from src.utils import validate_amount, validate_date
import shutil

expenses = load_expenses()

while True:
    show_menu()
    print("4. Generate Monthly Report")
    print("5. Search Expenses")
    print("6. Backup Data")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = input("Enter amount: ")
        if not validate_amount(amount):
            print("❌ Invalid amount")
            continue

        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        if not validate_date(date):
            print("❌ Invalid date")
            continue

        desc = input("Enter description: ")
        expenses.append(Expense(amount, category, date, desc))
        save_expenses(expenses)
        print("✅ Expense added successfully")

    elif choice == "2":
        for e in expenses:
            print(e)

    elif choice == "3":
        summary = category_summary(expenses)
        for k, v in summary.items():
            print(f"{k}: ₹{v}")

    elif choice == "4":
        year = int(input("Enter year (YYYY): "))
        month = int(input("Enter month (1-12): "))
        total = monthly_report(expenses, year, month)
        print(f"Total expense for {year}-{month}: ₹{total}")

    elif choice == "5":
        keyword = input("Enter keyword to search: ").lower()
        for e in expenses:
            if keyword in e.category.lower() or keyword in e.description.lower():
                print(e)

    elif choice == "6":
        shutil.copy(
            "finance-manager/data/expenses.csv",
            "finance-manager/data/expenses_backup.csv"
        )
        print("✅ Backup created successfully")

    elif choice == "7":
        print("Goodbye!")
        break

