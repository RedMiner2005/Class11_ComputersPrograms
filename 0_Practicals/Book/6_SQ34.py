# Computers Practical Programs

"""WAP to print the following pattern:
5 5 5 5 
5 5 5 5 
5 5 5 5 
5 5 5 5 
"""

i = 3
while (i >= 0):
    j = 3
    while (j >= 0):
        print(5, end=" ")
        j = j - 1
    print()
    i = i - 1
