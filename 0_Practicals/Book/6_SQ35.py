# Computers Practical Programs

"""WAP to print the following pattern:
1 2 3
1 2
1
"""

i = 3
while i >= 0:
    j = 1
    while j <= i:
        print(j, end=" ")
        j = j + 1
    print()
    i = i - 1
