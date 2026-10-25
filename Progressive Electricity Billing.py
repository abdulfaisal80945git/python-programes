n = int(input("Number of patients: "))

for i in range(n):
    name = input("Patient name: ")
    consultation = float(input("Consultation charge: "))
    tests = float(input("Diagnostic charges: "))
    treatment = float(input("Treatment charges: "))
    age = int(input("Patient age: "))

    total = consultation + tests + treatment

    if age >= 60:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    if final_bill <= 1000:
        category = "Low"
    elif final_bill <= 5000:
        category = "Medium"
    else:
        category = "High"

    if min(consultation, tests, treatment) < 0:
        print("Invalid charges")
    else:
        print("\nPatient:", name)
        print("Total:", round(total, 2))
        print("Discount:", round(discount, 2))
        print("Final Bill:", round(final_bill, 2))
        print("Category:", category)
