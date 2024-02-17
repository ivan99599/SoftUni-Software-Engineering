def orders(current_product, current_quantity, result):
    if current_product == "coffee":
        result = current_quantity * coffee
        return f"{result:.2f}"
    elif current_product == "water":
        result =  current_quantity * water
        return f"{result:.2f}"
    elif current_product == "coke":
        result = current_quantity * coke
        return f"{result:.2f}"
    elif current_product == "snacks":
        result =  current_quantity * snacks
        return f"{result:.2f}"


product = input()
quantity = int(input())
result = 0
coffee = 1.50
water = 1.00
coke = 1.40
snacks = 2.00
print(orders(product, quantity, result))