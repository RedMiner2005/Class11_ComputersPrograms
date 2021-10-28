# Practical Implementation - 4 : 28 Oct 2021

str1 = input("Enter a string: ")
print("Original string:", str1)
str2 = ""
x = str1.split()
for a in x:
    str2 += a.capitalize() + " "
print(str2)
