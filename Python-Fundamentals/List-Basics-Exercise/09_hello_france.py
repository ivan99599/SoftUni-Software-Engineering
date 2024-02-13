items_to_buy = input().split("|")
start_budget = float(input())

ticket_to_france_price = 150
total_sells = 0
current_budget = start_budget
sells_profit_total = 0
sell_price_list = []
for current_item in items_to_buy:
    item, price = current_item.split("->")
    price = float(price)
    if current_budget <= 0:
        break
    elif current_budget < price:
        continue
    elif (item == "Clothes" and (price <= 50)) or \
            (item == "Shoes" and (price <= 35)) or \
            (item == "Accessories" and (price <= 20.5)):
        sell_price = price * 1.40
        sell_price_list.append(sell_price)
        sells_profit_total += (sell_price - price)
        total_sells += sell_price
        current_budget -= price
final_budget = current_budget + total_sells

for item in sell_price_list:
    print(f"{item:.2f}", end=" ")
print()
print(f"Profit: {sells_profit_total:.2f}")
if final_budget >= ticket_to_france_price:
    print("Hello, France!")
else:
    print("Not enough money.")