import re


def main():
    s = input("Text: ")
    print(count(s))


def count(s):
    pattern = r"\bum\b"
    matches = re.findall(pattern, s, re.IGNORECASE)
    if matches:
        return len(matches)
    else:
        return 0


if __name__ == "__main__":
    main()
