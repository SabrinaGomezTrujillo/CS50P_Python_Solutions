import sys


def main():

    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) <= 1:
        print("Too few command-line arguments")
        sys.exit(1)
    else:  # len(sys.argv)==2
        filename = sys.argv[1]
        if not filename.endswith(".py"):
            print("Not a Python file")
            sys.exit(1)
        else:
            try:
                with open(filename, "r") as file:
                    print(count_rows(f=filename))
            except FileNotFoundError:
                #    raise FileNotFoundError
                print("File does not exist")
                sys.exit(1)


def count_rows(f):
    with open(f, "r") as file:
        row_count = 0
        for line in file:
            stripped_row = line.strip()
            if not stripped_row:
                continue
            if stripped_row.startswith("#"):
                continue
            else:
                row_count += 1
        return row_count


main()
