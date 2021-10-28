# Computers Practical Programs

"""WAP to perform the following tasks according to the user's choice using menu
a) Area of a circle
b) Area of a rectangle
c) Circumference of a circle
d) Area of a square"""

while True:
    print("1. For area of a circle")
    print("2. For area of a rectangle")
    print("3. For circumference of a circle")
    print("4. For area of a square")

    ch = int(input("Enter your choice (Enter 0 to exit): "))
    if ch == 1:
        r = int(input("Enter the radius of the circle: "))
        a = 3.14 * r * r
        print("Area of the circle:", a)
    elif ch == 2:
        l = int(input("Enter the length: "))
        b = int(input("Enter the breadth: "))
        a = l * b
        print("Area of the rectangle:", a)
    elif ch == 3:
        r = int(input("Enter the radius of the circle: "))
        c = 2 * (int(3.14 * r))
        print("Circumference of the circle:", c)
    elif ch == 4:
        l = int(input("Enter the side of the square: "))
        a = l * l
        print("Area of square:", a)
    elif ch == 0:
        break
    else:
        print("Invalid option!")
    print()