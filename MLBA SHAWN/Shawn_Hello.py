#
# Shawn, 2026/02/25
# Shawn_Hello.py
# Print Hello
#

#work1
name = "THU"

print("Hello", name)
print("How are you?")

#work2
price = 250
units_sold = 1200

total_sales = price * units_sold

print(f"Total Sales : ${total_sales: ,}")
discount = total_sales * 0.05      #5% discount
print(f"Discount : ${discount:,.2f}")
net_sales = total_sales - discount
print(f"Net Sales : ${net_sales:,.2f}")
print(type(3.14))

# if / elif / else
quarterly_profit = 85_000

if quarterly_profit > 100_000:
    print("Outstanding quarter — bonus approved.")
elif quarterly_profit > 50_000:
    print("Good quarter — on target.")
elif quarterly_profit > 0:
    print("Marginal quarter — review costs.")
else:
    print("Loss this quarter — action required.")

    # Combining conditions with 'and' / 'or'
customer_age  = 35
account_value = 120_000

if customer_age >= 30 and account_value >= 100_000:
    print("Eligible for premium wealth management services.")
else:
    print("Standard account services apply.")