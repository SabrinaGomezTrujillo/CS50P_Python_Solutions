def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/", 1)
            x_num = int(x)
            y_num = int(y)

            if y_num == 0:
                raise ZeroDivisionError
            if x_num > y_num:
                raise ValueError
            if x_num < 0 or y_num < 0:
                raise ValueError

            fuel = round((x_num / y_num) * 100)
            if fuel <= 1:
                print("E")
            elif fuel >= 99:
                print("F")
            else:
                print(f"{fuel}%")
            break

        except ValueError:
            print("ValueError")
        except ZeroDivisionError:
            print("ZeroDivisionError")

main()
