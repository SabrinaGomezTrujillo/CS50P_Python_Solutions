def main():
    pedido = {}

    try:
        while True:
            item = input().upper().strip()
            if item:
                if item in pedido:
                    pedido[item] += 1
                else:
                    pedido[item] = 1

    except EOFError:
        print("\n")
        for item in sorted(pedido):
            print(f"sorted.{pedido[item]} {item}")
main()
