def calchange(paid,price)
    change=paid-price
    return change
snackp=50
print("WELCOME TO SNACK VENDING MACHINE")
print("This snack costs u 50 rupees")
print("Accepted coins are=1,5,10,20")
totalin=0
coinin=0
while True:
    coin=int(input("insert the coin"))
    if coin!=1 and coin!=5 and coin!=10 and coin!=20:
        print("invalid coin")
        continue
    totalin+=coin
    coinin+=1
    print(f"inserted {coin} . total so far is {totalin}")
    if totalin>=snackp:
        print("Enough money inserted")
        break
changed=calchange(totalin,snackp)
print("dispensing your snack")
if changed==0:
    pass
else:
    print("Here is ur change:",changed)
print("PURCHASE SUMMARY")
print("Snack price=",snackp)
print("Coins inserted",coinin)
print("Total paid",totalin)
print("Change given=",changed)
print("Thank u , please visit again")

