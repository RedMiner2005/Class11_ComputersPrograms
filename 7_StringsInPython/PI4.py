# Practical Implementation - 4 : 22 Oct 2021

line = input("Enter a line: ")
lowercount = uppercount = 0
digicount = alphacount = 0
for a in line:
    if a.islower():
        lowercount += 1
    elif a.isupper():
        uppercount += 1
    elif a.isdigit():
        digicount += 1
    if a.isalpha():
        alphacount += 1
print("Number of uppercase letters:", uppercount)
print("Number of lowercase letters:", lowercount)
print("Number of alphabets:", alphacount)
print("Number of digits:", digicount)
