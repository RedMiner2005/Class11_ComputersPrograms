# Practical Implementation - 5 : 1 Oct 2021

"""A program to calculate the tax payable if salary is given"""
salary = int(input("Enter the salary of the person: "))
if salary <= 50000:
    tax = 0.05 * salary
elif salary <= 60000:
    tax = 0.07 * salary
elif salary <= 70000:
    tax = 0.08 * salary
else:
    tax = 0.10 * salary
print("Salary:", salary, "\nTax payable:", tax)
