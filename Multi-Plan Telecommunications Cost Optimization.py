n = int(input("Number of passengers: "))
total = 0

for i in range(n):
    age = int(input("Enter passenger age: "))
    distance = float(input("Enter travel distance in km: "))
    travel_class = input("Enter class (Sleeper/AC): ").lower()

    if travel_class == "sleeper":
        rate = 1
    else:
        rate = 2

    fare = distance * rate

    if age < 5:
        fare = 0
    elif age >= 60:
        fare = fare * 0.75

    fare = fare + 30  # Reservation fee

    cancel = input("Cancel ticket? (yes/no): ").lower()
    if cancel == "yes":
        fare = fare * 0.50

    print("Passenger fare: Rs.", round(fare, 2))
    total += fare

print("Total amount: Rs.", round(total, 2))
