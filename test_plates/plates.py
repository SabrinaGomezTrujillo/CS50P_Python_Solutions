def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2:
        return False
    if len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        raise ValueError


    if not s.isalnum():
      raise ValueError

    for i in range(len(s)):
        if s[i].isdigit():

            if s[i] == "0":
                return False

            for j in range(i + 1, len(s)):
                if not s[j].isdigit():
                    return False
            break
    return True


if __name__ == "__main__":
    main()
