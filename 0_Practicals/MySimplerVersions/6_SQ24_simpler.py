# Computers Practical Programs

"""Write a program to accept a character from the user and display whether it is a vowel or cosonant"""
"""These programs as well as the textbook version show that numbers, other characters as consonants"""

def v0():
    """The actually simpler verion"""
    ch = input("Enter a character (Only first character will be considered): ")[0]
    if ch.lower() in "aeiou":
        print(ch, "is a vowel")
    else:
        print(ch, "is a consonant")

def v0_2():
    """The actually simpler verion"""
    ch = input("Enter a character (Only first character will be considered): ")[0]
    if ch in "aeiouAEIOU":
        print(ch, "is a vowel")
    else:
        print(ch, "is a consonant")

def v1():
    if (ch := input("Enter a character (Only first character will be considered): ")[0]).lower() in "aeiou":
        print(ch, "is a vowel")
    else:
        print(ch, "is a consonant")

def v2():
    """Works with older Python versions (than 3.9), shorter version of v0"""
    ch = input("Enter a character (Only first character will be considered): ")[0]
    print(ch, "is a", "vowel" if (ch.lower() in "aeiou") else "consonant")

def v3():
    print((ch := input("Enter a character (Only first character will be considered): ")[0]), "is a", "vowel" if (ch.lower() in "aeiou") else "consonant")

v3()