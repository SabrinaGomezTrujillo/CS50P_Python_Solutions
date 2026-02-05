from datetime import date, datetime, time
import sys
import num2words


def main():

    dob=input("Date of birth: ")
    total_minutos = validate_date(dob)
    print(f"{conv_text(total_minutos)}")



def validate_date(dob):
    try:
        dob = datetime.strptime(dob, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date")
        sys.exit(1)
    # replace_words = calc_minutos(dob)

    if dob:
        fecha1 = datetime.combine(dob, time.min)
        fecha2 = datetime.combine(date.today(), time.min)  # imprime la fecha de hoy a las 00:00:00
        delta = fecha2 - fecha1
        total_minutos = delta.total_seconds() / 60  # segundos en un minuto = 60
        return total_minutos

def conv_text(total_minutos):
    num2words.num2words(total_minutos, lang="en")
    replace_words = num2words.num2words(total_minutos, lang="en").replace(" and ", " ")
    return f"{replace_words.capitalize()} minutes"


if __name__ == "__main__":
    main()
