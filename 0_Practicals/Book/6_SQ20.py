# Computers Practical Programs

"""WAP to find the largest number among the three inputted numbers"""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if(a > b):
    if(a > c):
        print(a, "is the largest number")
    else:
        print(c, "is the largest number")
else:
    if(b > c):
        print(b, "is the largest number")
    else:
        print(c, "is the largest number")
