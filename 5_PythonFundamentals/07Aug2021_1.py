"""This program allows you to run any of the different questions given in the textbook exercise question 10."""


# Questions
def first():
    x = 2
    y = 3
    x += y
    print(x, y)


def second():
    x = 8
    y = 2
    x += y
    y -= x
    print(x, y)


def third():
    a = 5
    b = 10
    a += a + b
    b *= a + b
    print(a, b)


def fourth():
    p = 10
    q = 20
    p *= q // 3
    q += p + q ** 2
    print(p, q)


def fifth():
    p = 5 / 2
    q = p * 4
    r = p + q
    p += p + q + r
    r += p + q + r
    q -= p + q * r
    print(p, q, r)


def sixth():
    p = 2 / 5
    q = p * 4
    r = p * q
    p += p + q - r
    r *= p - q + r
    q += p + q
    print(p, q, r)


# Main Program
def main():
    programs = [exit, first, second, third, fourth, fifth, sixth]
    while True:
        try:
            question = int(input("Enter the program number that you want to run (0: Exit, 1 - 6: Programs): "))
            if 0 > question or question > 6:
                raise ValueError
        except ValueError as e:
            print("Please enter a valid integer from 0 to 6.\n")
            continue
        programs[question]()
        print("\n")

if __name__ == "__main__":
    main()
