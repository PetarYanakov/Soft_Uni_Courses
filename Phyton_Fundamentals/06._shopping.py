budget = int(input())
command = input()

while command != "End":
    product_price = int(command)
    if budget < 0:
        print("You want in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")