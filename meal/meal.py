def main():

    time=input("What time is it?: ")

    time_converted = convert(time)

    if 7.0 <= time_converted <= 8.0:
        print("It's breakfast time!")
    elif 12 <= time_converted <= 13:
        print("It's lunch time!")
    elif 18 <= time_converted <= 19:
        print("It's dinner time!")



def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return round(float(hours + minutes/60), 2)

if __name__ == "__main__":
    main()
