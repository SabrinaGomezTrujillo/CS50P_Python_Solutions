from validator_collection import validators, checkers, errors


def main():
    s = input("What's your email address?: ")
    print(validation(s))


def validation(s):
    try:
        email = validators.email(s)
        if checkers.is_email(email):
            return "Valid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()
