# Practical Implementation - 1 - Variation 1 : 25 Nov 2021
# Program to find the second largest number in a list

N = int(input("Enter the number of elements in a list:\n"))
num = [int(input("Enter list values:\n")) for i in range(N)]
print("The original list is:", str(num)[1:-1].replace(",", ""))

num.sort()
print("The second largest element in the list is: ", num[-2])
