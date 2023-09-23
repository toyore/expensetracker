from expense import Expense
import calendar
import datetime


def main():
    print(f"This is a script")
    expense_file_path = "expenses.csv"
    budget = 2000

    # Get user to input their expense
    expense=get_user_expense()


    # Write user's input to a file
    save_expenses_to_file(expense, expense_file_path)

    # Read from the file and summarize expenses
    summarize_user_expense(expense_file_path, budget)
    pass


def get_user_expense():
    print("Getting user's Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = [
        'Home', 'Work', 'Education', 'Food', 'Fun', 'Misc'
    ]

    while True:
        print('Select a category: ')
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}, {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if i in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount= expense_amount)
            return new_expense
        else:
            print("Invalid category. Please try again")

   
        
    

def save_expenses_to_file(expense: Expense, expense_file_path):
    print(f"Saving user Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.category}, {expense.amount}\n")

def summarize_user_expense(expense_file_path, budget):
    print(f"Finally reading from file")
    expenses: list[Expense] = []
    #to covert our users expenses to an object so as to perform calculations, we use readlines
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
             #strip function is used to remove extra spaces
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(name=expense_name, category = expense_category, amount= float(expense_amount))
            print(line_expense)
            expenses.append(line_expense)
    #print(expenses)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    #print(amount_by_category)
    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}") 

    total_spent = sum([xpense.amount for xpense in expenses])
    print(f"You've spent ${total_spent:.2f} this month!") 

      #To get the current date
    now = datetime.datetime.now()

    #Get the number of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    #calculate the remaining number of days in the current month
    remaining_days = days_in_month - now.day  

    if total_spent > budget:
        over_spent = total_spent - budget
        print(f" You have exceeded your budget for this month by {over_spent}")  
        print(f"Owings: {over_spent}") 
        remaining_days = days_in_month - now.day 
        print("Remaining days in the current month:", remaining_days) 
    else:
        remaining_budget = budget - total_spent
        print(f"Budget_remaining: ${remaining_budget:.2f}")
        print("Remaining days in the current month:", remaining_days)
        daily_budget = remaining_budget / remaining_days
        print(f"Budget per day: ${daily_budget:.2f}")






if __name__ == '__main__':
    main()