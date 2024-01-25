budget = int(input())
total_spend = 0

while True:
    command = input()

    if command == "End":
        print(f"You bought everything needed.")
        break
    price_per_product = int(command)

    if total_spend + price_per_product > budget:
        print(f"You went in overdraft!")
        break

    total_spend += price_per_product