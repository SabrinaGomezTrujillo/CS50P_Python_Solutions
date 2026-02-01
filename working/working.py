import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to ([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM)$"
    match = re.search(pattern, s, re.IGNORECASE)
    if not match:
        raise ValueError
    else:
        hora_1 = match.group(1)
        minuto_1 = match.group(2)
        meridiano_1 = match.group(3)
        hora_2 = match.group(4)
        minuto_2 = match.group(5)
        meridiano_2 = match.group(6)
        if match and meridiano_1.upper() == "AM" and hora_1 != "12":
            hora_1 = hora_1.zfill(2)
        if match and meridiano_2.upper() == "AM" and hora_2 != "12":
            hora_2 = hora_2.zfill(2)
        if match and meridiano_1.upper() == "PM" and hora_1 != "12":
            hora_1 = int(hora_1) + 12
        if match and meridiano_2.upper() == "PM" and hora_2 != "12":
            hora_2 = int(hora_2) + 12
        if match and meridiano_2.upper() == "AM" and hora_2 == "12":
            hora_2 = "00"
        if match and meridiano_1.upper() == "AM" and hora_1 == "12":
            hora_1 = "00"
        if match and meridiano_1.upper() == "PM" and hora_1 == "12":
            hora_1 = "12"
        if match and meridiano_2.upper() == "PM" and hora_2 == "12":
            hora_2 = "12"
        if minuto_1 is None:
            minuto_1 = "00"
        if minuto_2 is None:
            minuto_2 = "00"
        return f"{hora_1}:{minuto_1} to {hora_2}:{minuto_2}"

if __name__ == "__main__":
    main()
