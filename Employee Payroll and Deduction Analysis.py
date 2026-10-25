sage = float(input("Enter monthly data usage in GB: "))
calls = float(input("Enter call minutes: "))
budget = float(input("Enter budget: "))

plans = [
    ["Basic", 199, 2, 200, 28],
    ["Standard", 399, 10, 500, 56],
    ["Premium", 599, 25, 1000, 84]
]

best = None

for p in plans:
    name, price, data, minutes, validity = p

    extra_data = max(0, usage - data) * 10
    extra_calls = max(0, calls - minutes) * 0.5
    total = price + extra_data + extra_calls

    if total <= budget and (best is None or total < best[1]):
        best = [name, total, validity]

if best:
    print("Best Plan:", best[0])
    print("Total Cost: Rs.", round(best[1], 2))
    print("Validity:", best[2], "days")
else:
    print("No plan fits the budget")
