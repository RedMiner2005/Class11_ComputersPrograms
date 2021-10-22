# Practical Implementation - 10 : 1 Oct 2021

"""A program to find the whether a given number is positive, negative or zero"""
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("The number is 0.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")
