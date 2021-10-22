# Solved Questions - 13 : 1 Oct 2021

"""Find the output of thee following code if user inputs the following values for year:
a) 2000  b) 1971"""
year = int(input("Enter 4-digit year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("Leap year")
    else:
        print("Not a Leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a Leap year")
