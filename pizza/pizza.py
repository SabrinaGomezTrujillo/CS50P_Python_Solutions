import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) > 2:
        print("To many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print ("Too few command-line arguments")
        sys.exit(1)
    else:
        filename=sys.argv[1]
        if not filename.endswith(".csv"):
            print("Not a CSV file")
            sys.exit(1)
        else:
            try:
                with open(filename, "r") as file:
                    reader=csv.DictReader(file)
                    datos=list(reader)
                    print(tabulate(datos, headers="keys", tablefmt="grid"))
            except FileNotFoundError:
                print("File does not exist")
                sys.exit(1)


if __name__ == "__main__":
    main()
