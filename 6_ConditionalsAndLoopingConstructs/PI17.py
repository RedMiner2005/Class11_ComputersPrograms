# Practical Implementation - 16 : 6 Oct 2021

"""A program to illustrate the concept of infinite loop in while loop statement"""
var = 1
while var == 1:
    num = int(input("Enter a number: "))
    print("You entered: ", num)
print("Goodbye")                # Will not be run
