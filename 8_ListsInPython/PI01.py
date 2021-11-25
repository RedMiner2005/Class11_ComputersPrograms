# Practical Implementation - 1 : 25 Nov 2021
# Program to find the second largest number in a list


print("Enter the number of elements in a list: ")
N = int(input())
i = 0
num = []

while i < N:
    print("Enter the number: ")
    num1 = int(input())
    num.append(num1)
    i += 1

print("The original list is: ", end=" ")
for i in range(N):
    print(num[i], end=" ")


if num[0] > num[1]:
    first, second = num[0], num[1]
else:
    first, second = num[1], num[0]
for x in num[2:]:
    if x > second:
        if x > first:
            second, first = first, x
        else:
            second = x

print()
print("The second largest element in the list is: ", second)