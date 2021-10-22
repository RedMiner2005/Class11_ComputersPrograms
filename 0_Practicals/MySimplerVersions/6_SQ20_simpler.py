# Computers Practical Programs - Simpler Method Tester

"""WAP to find the largest number among the three inputted numbers"""
from random import randint
from time import time


def mine(a, b, c):
    if(a > b and a > c):
        return a
    elif(b >= a and b > c):
        return b
    else:
        return c


def book(a, b, c):
    if(a > b):
        if(a > c):
            return a
        else:
            return c
    else:
        if(b > c):
            return b
        else:
            return c


is_equal = 1
t_i = time()

for i in range(100000):
    x = randint(-100, 100)
    y = randint(-100, 100)
    z = randint(-100, 100)

    tester = (mine(x, y, z) == book(x, y, z))
    if tester == 0:
        print(x, y, z)

    is_equal *= tester

time_taken = time() - t_i
print(bool(is_equal), time_taken)
