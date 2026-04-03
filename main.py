import json # 1. Import required to manipulate JSON
import os #Required to check if the file already exits from tabulate import tabulate
from tabulate import tabulate

nameFile = "expenses.json" #Name of the file where the data will be saved

def upload_of_data():
    #read the JSON files. If there is not data, return empty.
    if not os.path.exists(nameFile):
        return []
    try:
        with open(nameFile, "r", encoding='utf-8') as f:
            return json.load(f)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        print("File not found or corrupted")
        return []

def save_data(expenses):
    #save the current expenses list to a json file
    try:
        with open(nameFile, "w", encoding='utf-8') as f:
            json.dump(expenses, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"File not found or corrupted: {e}")

# Interface and logic function.
def show_menu():
    print("\n"+"=" * 35)
    print("PERSONAL EXPENSE TRACKER")
    print("="*35)
    print("1. Add an Expense")
    print("2. View All Expenses")
    print("3. Show Total Spending")
    print("4. View Spending by Category")
    print("5. Exit")
    print("="*35)


#Function to add a new expense
def add_expense(expenses):
    try:
        # 1. Get user input for the category.
        category = input("Please enter a category (Food, Travel, Shopping, etc): ").capitalize()

        # 2 Get user input for the amount.
        amount = float(input("Please enter amount spent ($): "))

        #3. Get user input for the note
        note = input("Please enter a short note (optional): ")

        #4. Create a new dictionary for this single expense
        expense = {"category": category, "amount": amount, "note": note}

        #5. Add the new dictionary to our main
        expenses.append(expense)
        save_data(expenses)
        print(f"✔️ Expense added: {category} - ${amount:.2f} - {note}")
    except ValueError as e:
        print(f"⚠️ Input Error: {e}")


# Function to view all expenses.
def view_expenses(expenses):
    #Check if there are no expenses yet
    if len(expenses) == 0:
        print("📭 No expenses added yet! Start by adding an expense")
        return

    print("--- All Expenses ---")

    headers = ["#", "Category", "Amount ($)", "Note"]

    table_data = []
    #Create a counter to keep track of numbering count=1
    for count, expense in enumerate(expenses, start=1):
        table_data.append([count, expense["category"], expense["amount"], expense["note"]])

    print(tabulate(table_data, headers=headers, tablefmt="grid", numalign="right"))

def total_spending(expenses):
    #Check if there are no expenses yet
    if len(expenses) == 0:
        print("📭 No expenses added yet! Start by adding an expense")
        return

    total = sum(expense["amount"] for expense in expenses)
    print(f"\n💰 Total spending: ${total:.2f}")

def spending_by_category(expenses):
    if len(expenses) == 0:
        print("No expenses added yet! Start by adding an expense")
        return

    category_totals = {}
    for expense in expenses:
        cat = expense["category"]
        category_totals[cat] = category_totals.get(cat, 0) + expense["amount"]

    print("--- Spending by Category ---")
        #---table by category---
    cat_headers = ["Category", "Total Spent ($)"]
    cat_data = [[cat, f"{total:.2f}"] for cat, total in category_totals.items()]
    total = sum(expense["amount"] for expense in expenses)
    for category in category_totals.items():
            print(f"{category}: {total}")
    print(tabulate(cat_data, headers=cat_headers, tablefmt="simple", numalign="right"))


def main():
    #start: upload the data in the beginning of the program
    expenses = upload_of_data()

    while True:
        show_menu()
        choice = input("Please choose an option: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_spending(expenses)
        elif choice == "4":
            spending_by_category(expenses)
        elif choice == "5":
            print("Thank you for using this program!")
            break
        else:
            print("⚠️ Please enter a valid option")


if __name__ == "__main__":
    main()
