event = input().split("|")
energy = 100
coins = 100

for current_event in event:
    event_name, number = current_event.split("-")
    number = int(number)
    if event_name == "rest":
        energy += number
        if energy > 100:
            energy = 100
            print(f"You gained {abs(energy - 100)} energy.")
        print(f"Current energy: {energy}.")
    elif event_name == "order":
        if energy >= 0:
            print(f"You earned {number} coins.")
            coins += number
            energy -= 30
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")

if energy > 0 and coins > 0:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")