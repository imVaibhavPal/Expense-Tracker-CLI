
import json
from datetime import date, datetime
from pathlib import Path
from collections import defaultdict

FILE = Path(__file__).with_name("expenses.json")


def load_expenses():
    if not FILE.exists():
        return []

    try:
        with FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read expenses.json.")
        return []


def save_expenses(expenses):
    try:
        with FILE.open("w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
    except OSError as error:
        print(f"Error saving expenses: {error}")


# MONTHLY EXPENSE REPORT
def monthly_expense_report():
    month = input(
        "Enter month (YYYY-MM, e.g. 2026-10): "
    ).strip()

    # Validate month format
    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month! Use YYYY-MM format.")
        return

    expenses = load_expenses()

    # Filter expenses for the selected month
    monthly_expenses = [
        expense for expense in expenses
        if expense.get("date", "").startswith(month)
    ]

    if not monthly_expenses:
        print(f"\nNo expenses found for {month}.")
        return

    # Calculate total and category-wise spending
    total = sum(
        float(expense["amount"])
        for expense in monthly_expenses
    )

    category_totals = defaultdict(float)

    for expense in monthly_expenses:
        category = expense.get("category", "Other")
        category_totals[category] += float(expense["amount"])

    # Find the highest expense
    highest_expense = max(
        monthly_expenses,
        key=lambda expense: float(expense["amount"])
    )

    # Display monthly report
    print("\n" + "=" * 45)
    print("          MONTHLY EXPENSE REPORT")
    print(f"          Month: {month}")
    print("=" * 45)

    print(f"Number of expenses : {len(monthly_expenses)}")
    print(f"Total spending     : Rs. {total:.2f}")
    print(
        f"Average expense    : Rs. "
        f"{total / len(monthly_expenses):.2f}"
    )

    print("\nCATEGORY-WISE SPENDING")
    print("-" * 45)

    for category, amount in sorted(
        category_totals.items(),
        key=lambda item: item[1],
        reverse=True
    ):
        percentage = (amount / total * 100) if total else 0

        print(
            f"{category:<18} Rs. {amount:>9.2f} "
            f"({percentage:5.1f}%)"
        )

    print("\nHIGHEST EXPENSE")
    print("-" * 45)
    print(
        f"Description : "
        f"{highest_expense.get('description', 'N/A')}"
    )
    print(
        f"Category    : "
        f"{highest_expense.get('category', 'Other')}"
    )
    print(
        f"Amount      : Rs. "
        f"{float(highest_expense['amount']):.2f}"
    )
    print(
        f"Date        : "
        f"{highest_expense.get('date', 'N/A')}"
    )
    print("=" * 45)


# ADD EXPENSE
def add_expense(expenses):
    try:
        amount = float(input("Enter amount: Rs. "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter category: ").strip()
        description = input("Enter description: ").strip()

        if not category:
            print("Category cannot be empty.")
            return

        expense = {
            "id": max(
                (e.get("id", 0) for e in expenses),
                default=0
            ) + 1,
            "amount": amount,
            "category": category,
            "description": description,
            "date": date.today().isoformat()
        }

        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid number.")


# VIEW ALL EXPENSES
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- ALL EXPENSES ---")

    for expense in expenses:
        print(
            f"ID: {expense['id']} | "
            f"Rs. {float(expense['amount']):.2f} | "
            f"{expense['category']} | "
            f"{expense['date']} | "
            f"{expense['description']}"
        )


# SHOW TOTAL EXPENSES
def show_total(expenses):
    total = sum(float(e["amount"]) for e in expenses)
    print(f"Total expenses: Rs. {total:.2f}")


# FILTER BY CATEGORY
def filter_category(expenses):
    category = input(
        "Enter category to search: "
    ).strip().lower()

    matches = [
        e for e in expenses
        if e.get("category", "").lower() == category
    ]

    if not matches:
        print("No expenses found in this category.")
        return

    view_expenses(matches)


# DELETE EXPENSE
def delete_expense(expenses):
    try:
        expense_id = int(
            input("Enter expense ID to delete: ")
        )

        for expense in expenses:
            if expense.get("id") == expense_id:
                expenses.remove(expense)
                save_expenses(expenses)
                print("Expense deleted successfully!")
                return

        print("Expense ID not found.")

    except ValueError:
        print("Please enter a valid ID.")


# MAIN MENU
def main():
    expenses = load_expenses()

    while True:
        print("\n" + "=" * 35)
        print("         EXPENSE TRACKER")
        print("=" * 35)
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Show total expenses")
        print("4. Filter by category")
        print("5. Delete expense")
        print("6. Monthly expense report")
        print("7. Exit")
        print("=" * 35)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            filter_category(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            monthly_expense_report()

        elif choice == "7":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
