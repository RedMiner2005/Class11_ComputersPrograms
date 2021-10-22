"""def celsius_to_fahrenheit(c: float) -> float:
    return float(1.8 * c + 32)


if __name__ == "__main__":
    while True:
        try:
            celsius = float(input("Enter the temperature in degree Celsius: "))
        except ValueError as e:
            print("Please type a vaild number.\n")
            continue
        print(f"{celsius} Celsius = {celsius_to_fahrenheit(celsius)} Fahrenheit")
        break"""


Celsius = float(input("Enter temperature in Celsius: "))
Fahrenheit = Celsius * 1.8 + 32                                  # Calclutae Fahrenheit
print("{} Celsius = {} Fahrenheit".format(Celsius, Fahrenheit))
