# Practical Implementation - 7 : 30 Sep 2021

"""A program to accept the percentage of a student and display grade"""
perc = float(input("Enter the percentage of the student: "))
if perc > 85:
    print("A")
elif perc > 70 and perc <= 85:
    print("B")
elif perc > 60 and perc <= 70:
    print("C")
elif perc > 45 and perc <= 60:
    print("D")
else:
    print("E")
