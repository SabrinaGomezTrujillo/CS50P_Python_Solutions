def main():
    time = input("What time is it? (HH:MM): ")

    if 7.0 <= convert(time) <= 8.0:
        print("It's breakfast time!")
    elif 12 <= convert(time) <= 13:
        print("It's lunch time!")
    elif 18 <= convert(time) <= 19:
        print("It's dinner time!")


def convert(time):
    hours, minutes = map(int, time.split(":"))
    return round(float(hours + minutes/60), 2)


if __name__ == "__main__":
    main()
