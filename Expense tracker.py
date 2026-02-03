import csv
import os

CSV_FILE = 'expenses.csv'
FIELDS = ['name', 'amount', 'category']

def load_expenses():
    expenses = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                expenses.append(row)
    return expenses

def save_expenses(expenses):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(expenses)

def add_expense(expenses):
    name = input("Expense name: ").strip()
    amount = input("Amount: ").strip()
    category = input("Category: ").strip()
    expenses.append({'name': name, 'amount': amount, 'category': category})
    save_expenses(expenses)
    print("Expense added.\n")

def delete_expense(expenses):
    name = input("Expense name to delete: ").strip()
    matches = [(i, e) for i, e in enumerate(expenses) if e.get('name') == name]
    if not matches:
        print("No matching expenses found.\n")
        return
    if len(matches) == 1:
        i, e = matches[0]
        confirm = input(f"Delete '{e['name']}' {e['amount']} {e['category']}? (y/N): ").strip().lower()
        if confirm == 'y':
            del expenses[i]
            save_expenses(expenses)
            print("Expense deleted.\n")
        else:
            print("Delete cancelled.\n")
        return
    # multiple matches: list and choose
    print("Multiple matches found:")
    for idx, (i, e) in enumerate(matches, start=1):
        print(f"{idx}. {e['name']:20} {e['amount']:10} {e['category']:15}")
    choice = input("Choose number to delete (or blank to cancel): ").strip()
    if not choice:
        print("Delete cancelled.\n")
        return
    try:
        sel = int(choice)
        if sel < 1 or sel > len(matches):
            raise ValueError
    except ValueError:
        print("Invalid selection.\n")
        return
    del expenses[matches[sel-1][0]]
    save_expenses(expenses)
    print("Expense deleted.\n")

def edit_expense(expenses):
    name = input("Expense name to edit: ").strip()
    matches = [(i, e) for i, e in enumerate(expenses) if e.get('name') == name]
    if not matches:
        print("No matching expenses found.\n")
        return
    if len(matches) == 1:
        i, e = matches[0]
    else:
        print("Multiple matches found:")
        for idx, (i2, e2) in enumerate(matches, start=1):
            print(f"{idx}. {e2['name']:20} {e2['amount']:10} {e2['category']:15}")
        choice = input("Choose number to edit (or blank to cancel): ").strip()
        if not choice:
            print("Edit cancelled.\n")
            return
        try:
            sel = int(choice)
            if sel < 1 or sel > len(matches):
                raise ValueError
        except ValueError:
            print("Invalid selection.\n")
            return
        i, e = matches[sel-1]
    print("Leave blank to keep current value.")
    new_name = input(f"Name [{e['name']}]: ").strip()
    new_amount = input(f"Amount [{e['amount']}]: ").strip()
    new_category = input(f"Category [{e['category']}]: ").strip()
    if new_name:
        expenses[i]['name'] = new_name
    if new_amount:
        expenses[i]['amount'] = new_amount
    if new_category:
        expenses[i]['category'] = new_category
    save_expenses(expenses)
    print("Expense updated.\n")

def list_expenses(expenses):
    if not expenses:
        print("No expenses found.\n")
        return
    print(f"{'Name':20} {'Amount':10} {'Category':15}")
    print("-" * 45)
    for exp in expenses:
        print(f"{exp['name']:20} {exp['amount']:10} {exp['category']:15}")
    print()

def main():
    expenses = load_expenses()
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Delete Expense")
        print("4. Edit Expense")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            list_expenses(expenses)
        elif choice == '3':
            delete_expense(expenses)
        elif choice == '4':
            edit_expense(expenses)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()