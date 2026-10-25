venue = float(input("Venue cost: "))
equipment = float(input("Equipment cost: "))
catering = float(input("Catering cost per participant: "))
transport = float(input("Transport cost per participant: "))
certificate = float(input("Certificate cost per participant: "))

sponsor = float(input("Sponsorship amount: "))
fee = float(input("Registration fee per participant: "))
participants = int(input("Expected participants: "))

fixed_cost = venue + equipment
variable_cost = catering + transport + certificate
total_cost = fixed_cost + variable_cost * participants
income = sponsor + fee * participants

print("Total Cost: Rs.", round(total_cost, 2))
print("Total Income: Rs.", round(income, 2))
print("Surplus/Deficit: Rs.", round(income - total_cost, 2))

if fee > variable_cost:
    required = max(0, int((fixed_cost - sponsor) / (fee - variable_cost)) +
                   (1 if (fixed_cost - sponsor) % (fee - variable_cost) != 0 else 0))
    print("Minimum participants to break even:", required)
elif sponsor >= fixed_cost:
    print("Sponsorship covers fixed costs.")
else:
    print("Break-even is not possible at this registration fee.")
