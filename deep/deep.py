answer=input("What is the answer to the Great Question of Life, the Universe and Everything? ")

if answer == "42" or answer.lower().replace(" ","") == "fortytwo" or answer.lower() == "forty-two":
    print("Yes")

else:
    print("No")
