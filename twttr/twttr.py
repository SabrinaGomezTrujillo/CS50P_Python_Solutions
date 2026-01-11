def main():
    text = input("Input:")
    x_text=""
    vocales = ["a","e","i","o","u"]

    for letter in text:
        if letter.lower() not in vocales:
            x_text+=letter
    print(f"Outpu: {x_text}")
main()
