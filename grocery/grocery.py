def main():
    pedido = {}

    try:
        while True:
            # Pedir palabra por palabra
            item = input().upper().strip()

            if item:  # Si no está vacío
                if item in pedido:
                    pedido[item] += 1
                else:
                    pedido[item] = 1
    except EOFError:
         print("""\n""")
         for item in sorted(pedido):
#            print(sorted(pedido.keys()))
            print(f"{pedido[item]} {item}")
main()
