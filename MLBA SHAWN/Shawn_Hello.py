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