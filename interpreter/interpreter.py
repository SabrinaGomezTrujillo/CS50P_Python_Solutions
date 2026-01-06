expression = input("Expression: ")
x, y, z = expression.split(" ")

match y:
    case "+":
        print(f"{int(x) + int(z):,.1f}")
    case "-":
        print(f"{int(x) - int(z):,.1f}")
    case "*":
        print(f"{int(x) * int(z):,.1f}")
    case "/":
        if int(z) == 0:
            print("Division by 0!")
        else:
            print(f"{int(x) / int(z):,.1f}")
    case _:
        print("Unknown operator")  
