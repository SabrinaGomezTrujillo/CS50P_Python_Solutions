text=input()
def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")
def main(text):
    print(convert(text))
main(text)

