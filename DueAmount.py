
bill_amount = float(input("Enter total bill amount: "))

payment_amount = float(input("Enter payment amount: "))

due_amount = bill_amount - payment_amount

if due_amount > 0:
    print(f"Payment successful. Remaining due: ${due_amount:.2f}")
elif due_amount == 0:
    print("Bill fully paid.")
else:
    print(f"Payment successful. Change to return: ${abs(due_amount):.2f}")
