def order(products, quantity):
    if product == "coffee":
        return 1.50 * quantity
    if product == "coke":
        return 1.40 * quantity
    if product == "water":
        return 1 * quantity
    if product == "snacks":
        return 2 * quantity


product = input()
quantity = int(input())
result = order(product, quantity)
print(f"{result:.2f}")