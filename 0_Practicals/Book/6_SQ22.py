# Computers Practical Programs

"""WAP that reads two numbers and an arithmetic operator and displays the results"""

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
op = input("Enter the operator: ")

if (op == "+"):
    print(a + b)
elif (op == "-"):
    print(a - b)
elif (op == "*"):
    print(a * b)
elif (op == "/"):
    print(a / b)
elif (op == "%"):
    print(a % b)
elif (op == "**"):
    print(a ** b)
else:
    print("Invalid option!")
