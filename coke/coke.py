def main():
    money=[]
    coke_v=int(50)
    while True:
            insert=int(input("Insert Coin: "))
            money.append(insert)
            Due=int(coke_v-sum(money))
            Owe=int(sum(money)-coke_v)
            if coke_v>Due>0:
                print(f"Amount Due: {Due}")
            if Due<=0:
                print(f"Change Owed: {Owe}")
                break
main()
