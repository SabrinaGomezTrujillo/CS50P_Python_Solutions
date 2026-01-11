def main():
    camel = input("camelCase: ")
    snake = ""

    for letra in camel:
        if letra.isupper():
            snake += "_" + letra.lower()
        else:
            snake += letra
    print(f"snake_case: {snake}")

if __name__ == "__main__":
    main()
