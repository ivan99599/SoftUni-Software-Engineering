elements = input().split()
stock = {}
for index in range(0, len(elements), 2):
    key = elements[index]
    value = elements[index + 1]
    stock[key] = int(value)
products = input().split()
for product in products:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")



