# Practical Implementation - 14 : 6 Oct 2021

"""A program to accept a number from a user and print factorial of that number."""
num = int(input("Enter a non-negative number to take factorial of: "))
fact = 1
for i in range(num):
    fact *= i + 1
print("Factorial of", num, "=", fact)
