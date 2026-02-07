import csv
import os
from src.expense import Expense

FILE_PATH = "finance-manager/data/expenses.csv"

def load_expenses():
    expenses = []
    if not os.path.exists(FILE_PATH):
        return expenses

    with open(FILE_PATH, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(
                Expense(row['Amount'], row['Category'], row['Date'], row['Description'])
            )
    return expenses

def save_expenses(expenses):
    with open(FILE_PATH, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])
        for e in expenses:
            writer.writerow(e.to_list())
