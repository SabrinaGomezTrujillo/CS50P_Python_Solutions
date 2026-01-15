
def main():
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    while True:
        fecha = input("Date: ").strip()
        if "/" in fecha:
            try:
                m, d, y = fecha.split("/")
                mes = int(m)
                dia = int(d)
                año = int(y)

                if 1 <= mes <= 12 and 1 <= dia <= 31:
                    print(f"{año:04d}-{mes:02d}-{dia:02d}")
                    break
            except:
                pass

        elif "," in fecha:
            try:
                parte1, parte2 = fecha.split(",")
                año = int(parte2.strip())

                parte1 = parte1.strip()
                if " " in parte1:
                    mes_str, dia_str = parte1.split(" ")
                    mes_str = mes_str.title()
                    dia = int(dia_str)

                    if mes_str in months:
                        mes = months.index(mes_str) + 1

                        if 1 <= dia <= 31:
                            print(f"{año:04d}-{mes:02d}-{dia:02d}")
                            break
            except:
                pass

main()
