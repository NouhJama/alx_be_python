monthly_income = int(input("What is your monthly income? "))
total_monthly_expenses = int(input("What are your total monthly expenses? "))
monthly_savings = monthly_income - total_monthly_expenses

interest_rate = 0.05
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * interest_rate)

print(f"Your monthly savings are: {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {annual_savings:.0f}.")