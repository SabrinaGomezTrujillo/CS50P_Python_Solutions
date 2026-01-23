import inflect

p = inflect.engine()


def main():
    aurevoir = []
    while True:
        try:
            x = input("Name: ")
            aurevoir += [x]
        except EOFError:
            print(f"\nAdieu, adieu, to {p.join(aurevoir)}")
            break


main()
