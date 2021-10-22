# Computers Practical Programs

"""WAP to print the following pattern:
A
B C 
D E F 
G H I J 
K L M N O
"""

i = 1
num = 65
while i <= 5:
    j = 1
    while j <= i:
        print(chr(num), end=" ")
        j = j + 1
        num = num + 1
    print()
    i = i + 1
