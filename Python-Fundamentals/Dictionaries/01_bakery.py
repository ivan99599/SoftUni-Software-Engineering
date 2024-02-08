elements = input().split()
bakery = {}

for index in range(0, len(elements), 2):
    food = elements[index]
    quantities = elements[index + 1]
    bakery[food] = int(quantities)

print(bakery)



