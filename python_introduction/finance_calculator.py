# Get user input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected savings after 1 year with 5% interest
# Formula: (monthly_savings × 12) + (monthly_savings × 12 × 0.05)
annual_savings_no_interest = monthly_savings * 12
interest_earned = annual_savings_no_interest * 0.05
projected_savings = annual_savings_no_interest + interest_earned

# Alternative one-liner (same result):
# projected_savings = monthly_savings * 12 * 1.05

# Display results in the exact required format
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")