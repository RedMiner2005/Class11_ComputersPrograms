# Computers Practical Programs

"""WAP to print the following pattern:
A
B C 
D E F 
G H I J 
K L M N O
"""


def v1(rows: int):
    for i in range(rows):
        for j in range(i + 1):
            print(chr(65 + j + (i * (i + 1) // 2)), end=" ")
        print()


def v1_2(rows: int):
    for i in range(rows):
        for j in range(i + 1):
            print(chr(65 + j + sum(range(i + 1))), end=" ")
        print()


def v2(rows: int):
    """Same as before, but condensed in a single line, against PEP 8"""
    print(*((" ".join(chr(65 + j + sum(range(i + 1))) for j in range(i + 1))) for i in range(rows)), sep="\n")


v2(5)
