gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break

    action, *args = command.split()

    if action == "OutOfStock":
        gift = args[0]
        gifts = ['None' if g == gift else g for g in gifts]
    elif action == "Required":
        gift, index = args
        index = int(index)
        if 0 <= index < len(gifts):
            gifts[index] = gift
    elif action == "JustInCase":
        gifts[-1] = args[0]

result = ' '.join(filter(lambda g: g != 'None', gifts))
print(result)






