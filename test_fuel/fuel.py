def main():
    fraction = input("Fraction: ")
    try:
        fuel = convert(fraction)
        print(gauge(fuel))
    except (ValueError, ZeroDivisionError) as e:
        print(type(e).__name__)


def convert(fraction):
    try:
        x, y = fraction.split("/", 1)
        x_num = int(x)
        y_num = int(y)

        if y_num == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        if x_num < 0 or y_num < 0:
            raise ValueError("Numbers cannot be negative")

        if x_num > y_num:
            raise ValueError("Numerator cannot be greater than denominator")

        return round((x_num / y_num) * 100)

    except ValueError:

        raise ValueError("Invalid input format")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
