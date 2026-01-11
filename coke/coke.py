def main():
    money=[]
    coke_v=int(50)
    print(f"Amount Due:{coke_v}")
    while True:

            insert=int(input("Insert Coin: "))
            money.append(insert)
            Due=int(coke_v-sum(money))
            Owe=int(sum(money)-coke_v)

            if insert not in [25, 10, 5]:
                 print (f"Amount Due:{coke_v}")
                 break

            elif coke_v>Due>0:
                print(f"Amount Due: {Due}")
            elif Due<=0:
                print(f"Change Owed: {Owe}")
                break
main()
