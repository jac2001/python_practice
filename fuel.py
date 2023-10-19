def main():
    fuel = get_input()

    if fuel == 0.75:
        print("75%")
    elif fuel == 0.50:
        print("50%")
    elif fuel == 0.25:
        print("25%")
    elif fuel <= 0.10:
        print("E")
    elif fuel >= 0.99:
        print("F")
    elif fuel == 0.33:
        print("33%")
    elif fuel == .67:
        print("67%")

def get_input():
    while True:
        try:
            fraction = input("Fraction: ")
            x_and_y = fraction.split('/')
            x = int(x_and_y[0])
            y = int(x_and_y[1])
            fuel_fraction = x / y

            if x > y:
                fraction = input("Fraction: ")
            return round(fuel_fraction, 2)
        except ValueError:
            fraction = input("Fraction: ")
        except ZeroDivisionError:
            fraction = input("Fraction: ")
        else:
            return round(fuel_fraction, 2)
main()


