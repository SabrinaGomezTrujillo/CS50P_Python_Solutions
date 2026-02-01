import re


def main():
    s = input("HTML: ")
    print(parse(s))


def parse(s):
    pattern = r"<iframe(?:.*)src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)\".*?></iframe>$"
    match = re.search(pattern, s, re.IGNORECASE)
    if match:
        return f"https://youtu.be/{match.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()
