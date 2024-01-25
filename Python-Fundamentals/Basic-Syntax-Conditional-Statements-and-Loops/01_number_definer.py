number = float(input())

if number == 0:
    print("zero")
elif number > 0:
    if 1 > abs(number) != 0:
        print(f"small positive")
    elif abs(number) > 1000000:
        print(f"large positive")
    else:
        print("positive")

elif number < 0:
    if 1 > abs(number) != 0:
        print(f"small negative")
    elif abs(number) > 1000000:
        print(f"large negative")
    else:
        print("negative")