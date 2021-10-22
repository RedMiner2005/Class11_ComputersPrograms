# Computers Practical Programs

"""WAP to print the following pattern:
5 5 5 5 
5 5 5 5 
5 5 5 5 
5 5 5 5 
"""


def v1():
    for i in range(4):
        for j in range(4):
            print(5, end=" ")
        print()


def v2():
    print(*(["5 " * 4] * 4), sep="\n")


v1()
