# Practical Implementation - 6 : 1 Oct 2021

"""A program to find the absolute value of a number in Python"""
numn = int(input("Enter a number (numerator): "))
numd = int(input("Enter a number (deominator): "))

if numn % numd == 0:
    print("\n" + str(numn) + " is divisible by " + str(numd))
else:
    print("\n" + str(numn) + " is not divisible by " + str(numd))
