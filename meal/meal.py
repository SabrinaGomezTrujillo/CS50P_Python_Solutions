time=input("What time is it? (HH:MM): ")
hours, minutes = map(int, time.split(":"))

def convert(time):
        return round(float(hours + minutes/60), 1)

#print(hours + minutes/60)
def main():

    if 7.0 <= convert(time) <= 8.0:
        print("It's breakfast time!")
    elif 12 <= convert(time) <= 13:
        print("It's lunch time!")
    elif 18 <= convert(time) <= 19:
        print("It's dinner time!")
    else:
        time

main()

