actual = input("Enter the correct answer sequence: ")
mine = input("Enter your answers: ")

if len(actual) != len(mine):
    print("The lengths of both the strings are not equal.")
    exit()

for i in range(len(mine)):
    if actual[i] == " ":
        print("Question number", i + 1, "has been skipped.")
        continue
    if not (mine[i] == " " or mine[i] == actual[i]):
        print("Incorrect:", i + 1)

input()