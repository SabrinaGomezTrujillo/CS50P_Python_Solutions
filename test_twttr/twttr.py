def main():
    text = input("Input:")
    print(f"Output: {shorten(text)}")

def shorten(word):
    x_text=""
    for letter in word:
        if letter.lower() not in ["a","e","i","o","u"]:
            x_text += letter
    return x_text

if __name__ == "__main__":
    main()
