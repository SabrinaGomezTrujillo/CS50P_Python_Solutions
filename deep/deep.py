text=input("What is the answer to the Great Question of Life, the Universe and Everything? ")
if text == "42":
    print("Yes")
elif text.lower() == "forty-two":
    print("Yes")
elif text.lower() == "forty two":
    print("Yes")
else:
    print("No")
