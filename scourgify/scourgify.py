import sys
import csv


def main():
    if len(sys.argv) > 3:
        print("To many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    filename = sys.argv[1]
    file2name = sys.argv[2]
    if not filename.endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    else:
        try:
            with open(filename, "r") as file, open(file2name, "w") as newfile:
                reader = csv.DictReader(file)
                writer = csv.DictWriter(newfile, fieldnames=["first","last","house"])
                writer.writeheader()

                for row in reader:
                    name = row["name"]
                    name2, name1 = row["name"].split(",")
                    first = name1.strip()
                    last = name2.strip()
                    newrow = {"first": first, "last": last, "house": row["house"]}
                    writer.writerow(newrow)

        except FileNotFoundError:
            print(f"Could not read {filename}")
            sys.exit(1)


if __name__ == "__main__":
    main()
