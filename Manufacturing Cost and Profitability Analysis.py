qty = int(input("Enter production quantity: "))
material = float(input("Material cost per unit: "))
labour = float(input("Labour cost per unit: "))
machine = float(input("Machine cost per unit: "))
wastage = float(input("Wastage percentage: "))
selling = float(input("Selling price per unit: "))
target = float(input("Target profit: "))

material_cost = qty * material
wastage_cost = material_cost * wastage / 100
labour_cost = qty * labour
machine_cost = qty * machine

total_cost = material_cost + wastage_cost + labour_cost + machine_cost
revenue = qty * selling
profit = revenue - total_cost

print("Total Cost: Rs.", round(total_cost, 2))
print("Revenue: Rs.", round(revenue, 2))
print("Profit: Rs.", round(profit, 2))

if profit >= target:
    print("Profit target achieved")
else:
    print("Profit target not achieved")
