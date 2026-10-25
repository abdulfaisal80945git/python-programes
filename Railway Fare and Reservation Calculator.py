n = int(input("Number of products: "))
total = 0

for i in range(n):
    name = input("Product name: ")
    category = input("Category (food/electronics/other): ").lower()
    price = float(input("Price: "))
    qty = int(input("Quantity: "))

    amount = price * qty

    if category == "food":
        tax = amount * 0.05
    elif category == "electronics":
        tax = amount * 0.18
    else:
        tax = amount * 0.12

    total += amount + tax

if total >= 5000:
    discount = min(total * 0.10, 1000)
elif total >= 2000:
    discount = total * 0.05
else:
    discount = 0

final_bill = total - discount

print("\n--- Retail Invoice ---")
print("Subtotal and tax: Rs.", round(total, 2))
print("Discount: Rs.", round(discount, 2))
print("Final Bill: Rs.", round(final_bill, 2))
