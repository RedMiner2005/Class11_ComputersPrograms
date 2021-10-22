"""
Python program to find the area and perimeter of a rectangle
"""


def mine():
    while True:
        try:
            l = float(input("Please enter the length of the rectangle: "))
            b = float(input("Please enter the breadth of the rectangle: "))
        except ValueError as e:
            print("Invalid input. Please enter a number.\n")
            continue
        print(f"Area of the rectangle: {l * b}\nPerimeter of the rectangle: {2 * (l + b)}")


# Input the dimensions of the rectangle.
length = float(input("Please enter the length of the rectangle: "))
breadth = float(input("Please enter the breadth of the rectangle: "))

# Calculate the area and perimeter of the rectangle
area = length * breadth
perimeter = 2 * (length + breadth)

# Print the area and perimeter
# print(f"\nArea of the rectangle: {area}\nPerimeter of the rectangle: {perimeter}")
print("Area of the rectangle:", area, "\nPerimeter of the rectangle:", perimeter)
