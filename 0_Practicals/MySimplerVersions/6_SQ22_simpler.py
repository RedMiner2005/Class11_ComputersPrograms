# Computers Practical Programs

"""WAP that reads two numbers and an arithmetic operator and displays the results"""

try:
    eval(input("Enter the first number: ") + input("Enter the operator: ") + input("Enter the second number: "))
except:
    print("Invalid option/number!")
