import sys
import random


def main():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        except ValueError:
            continue

    target = random.randint(
        1, n
    )  # verificar si es inclusivo o no arranca en 0 o 1? return

    while True:
        try:
            guess = int(input("Guess: "))
            if guess <=0:
                continue
            else:
                if guess < target:
                    print(f"Too small!")
                elif guess > target:
                    print(f"Too large!")
                else:
                    print(f"Just right!")
                    sys.exit()
        except ValueError:
            continue


main()
