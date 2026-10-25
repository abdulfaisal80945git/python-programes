n = int(input("Enter number of students: "))
students = []

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter aggregate marks: "))
    m1 = float(input("Enter subject 1 marks: "))
    m2 = float(input("Enter subject 2 marks: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter family income: "))

    if (marks >= 75 and m1 >= 40 and m2 >= 40
        and attendance >= 75 and income <= 200000):
        students.append([name, marks, attendance])

students.sort(key=lambda x: (-x[1], -x[2], x[0]))

print("\nEligible Students - Rank List")
for rank, s in enumerate(students, 1):
    print(rank, s[0], s[1], s[2])
