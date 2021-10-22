"""
>>> "Hello Python"
'Hello Python'
>>> print("Welcome to Python programming!")
Welcome to Python programming!
>>> print(10, 20, 30)  # Space is the default seperator
10 20 30
>>> print(10, 20, 30, sep="*")  # Here, * is used as the separator
10*20*30
>>> print(10, 20, 30, sep="-*-")
10-*-20-*-30
>>> print(10, 20, 30, sep=", ")
10, 20, 30
>>> print(10, 20, 30, sep="\n")
10
20
30
>>> print(10, 20, 30, sep="\t")
10	20	30
>>> print("Hello", "Hi", "Bonjour", sep=", ", end="!\n")
Hello, Hi, Bonjour!
>>> print(10 + 95)
105
>>> print(20/4 * 5 + 8 - 10)
23.0
>>> print(22/7)
3.142857142857143
>>> print(3.14 * 5 * 2)
31.400000000000002

"""

print("This is my 'n'th program.")
print("Using Python Script Mode")
print("It is advantageous over Interactive Mode")
print("It saves the statements typed using this mode.")
































# Simple Encryption
def encrypt(text):
	letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
	result = ""
	for l in text:
		result += "a" if l == " " else letters[letters.index(l) + 1]
	return result
