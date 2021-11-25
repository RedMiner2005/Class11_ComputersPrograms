"""To find at least one common element amongst two inputted lists"""


def book(list1, list2):
    for x in list1:
        for y in list2:
            if x == y:
                print("The common element is: ", x)


def mine1(list1, list2):
    for x in list1:
        if x in list2:
            print("The common element is: ", x)


def mine2(list1, list2):
    [print("The common element is: ", x) for x in list1 if x in list2]


def main():
    list1 = [1, 100, 200, 3, 5, 400]
    list2 = [2, 10, 300, 4, 5, 500]

    print("The elements in list1 are: ", list1)
    print("The elements in list2 are: ", list2)

    book(list1, list2)
    mine1(list1, list2)
    mine2(list1, list2)


if __name__ == "__main__":
    main()
