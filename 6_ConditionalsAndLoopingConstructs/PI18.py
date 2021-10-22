# Practical Implementation - 16 : 6 Oct 2021

"""A program to illustrate the concept of nested while loops"""
i = 2
while i >= 0:
    j = 2
    while j >= 0:
        print(2, end = " ")
        j -= 1
    print()
    i -= 1
