from datetime import datetime

def total_expense(expenses):
    return sum(e.amount for e in expenses)

def average_expense(expenses):
    return total_expense(expenses) / len(expenses) if expenses else 0

def category_summary(expenses):
    summary = {}
    for e in expenses:
        summary[e.category] = summary.get(e.category, 0) + e.amount
    return summary

def monthly_report(expenses, year, month):
    total = 0
    for e in expenses:
        date = datetime.strptime(e.date, "%Y-%m-%d")
        if date.year == year and date.month == month:
            total += e.amount
    return total
