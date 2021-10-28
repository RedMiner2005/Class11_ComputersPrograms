# Practical Implementation - 3 : 28 Oct 2021

"""Program to input name anf print the pattern as given below using string slicing: (if name is 'ANAND'), output should be:
A
AN
ANA
ANAN
ANAND
"""

name = input("Enter any name: ")
for i in range(0, len(name) + 1):
    print(name[0:i])
