bills = []

for month in range(1, 4):
    units = float(input("Enter units consumed: "))

    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    else:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed = 50
    surcharge = energy * 0.05
    rebate = 20 if units < 100 else 0
    total = energy + fixed + surcharge - rebate

    bills.append(total)
    print("Month", month, "Bill: Rs.", round(total, 2))

for i in range(1, len(bills)):
    if bills[i] > bills[i - 1] * 1.5:
        print("Unusual increase in month", i + 1)
