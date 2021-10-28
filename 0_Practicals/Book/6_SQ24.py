# Computers Practical Programs

"""Write a program to accept a character from the user and display whether it is a vowel or cosonant"""

ch = input("Enter a character: ")
if (ch == 'a' or ch == 'A'):
    print(ch, "is a vowel")
elif (ch == 'e' or ch == "E"):
    print(ch, "is a vowel")
elif (ch == 'i' or ch == "I"):
    print(ch, "is a vowel")
elif (ch == 'o' or ch == "O"):
    print(ch, "is a vowel")
elif (ch == 'u' or ch == "U"):
    print(ch, "is a vowel")
else:
    print(ch, "is a consonant")
