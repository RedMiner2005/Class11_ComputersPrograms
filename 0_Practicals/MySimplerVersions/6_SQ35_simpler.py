# Computers Practical Programs

"""WAP to print the following pattern:
1 2 3
1 2
1
"""


def v1(l):
    for i in range(l, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()


def v2(l):
    print("\n".join((" ".join(map(str, range(1, i+1)))) for i in range(l, 0, -1)))


v2(3)
