# Practical Implementation - 1 - Variation 1 : 25 Nov 2021
# Program to find the second largest number in a list

N = int(input("Enter the number of elements in a list:\n"))
num = []
for i in range(N):
    num.append(int(input("Enter list values:\n")))
print("The original list is:", " ".join(num))
first = num[num[0] < num[1]]
second = num[num[0] > num[1]]
for x in num[2:]:
    if x > second:
        if x > first:
            second, first = first, x
        else:
            second = x
print("The second largest element in the list is: ", second)
