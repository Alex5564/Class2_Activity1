actual_cost=float(input("Enter Actual_cost=  "))
selling_price=float(input("Enter Selling_price=  "))
 
if selling_price>actual_cost: 
 amount= selling_price-actual_cost
 print(f"float of: {amount}")
else:
 print("No profit")