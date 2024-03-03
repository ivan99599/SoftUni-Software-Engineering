items = {"shards": 0, "fragments": 0, "motes": 0}
information = input().split()
obtained = False

while not obtained:
    for index in range(0, len(information), 2):
        value = int(information[index])
        key = information[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            print(f"Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print(f"Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print(f"Dragonwrath obtained!")
            obtained = True
            items["motes"] -= 250
        if obtained:
            break
    if obtained:
        break
    information = input().split()

for material, quantity in items.items():
    print(f"{material}: {quantity}")