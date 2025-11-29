def finance_tracker():
    try:
        income = float(input("Enter your monthly income: "))

        expenses = []
        n = int(input("How many expenses? "))
        for i in range(n):
            amt = float(input(f"Enter expense {i+1}: "))
            expenses.append(amt)

        total_exp = sum(expenses)
        savings = income - total_exp
        percent_spent = (total_exp / income) * 100

        print("\n--- Finance Summary ---")
        print("Total Income:", income)
        print("Total Expenses:", total_exp)
        print("Savings:", savings)
        print("Percentage Spent: {:.2f}%".format(percent_spent))

        # Categorization
        if percent_spent < 40:
            cat = "LOW"
            msg = "Good control!"
        elif percent_spent < 70:
            cat = "MODERATE"
            msg = "Be careful!"
        else:
            cat = "HIGH"
            msg = "Financial Risk!"

        print("Category:", cat)
        print("Suggestion:", msg)

    except Exception as e:
        print("Error occurred:", e)

finance_tracker()
