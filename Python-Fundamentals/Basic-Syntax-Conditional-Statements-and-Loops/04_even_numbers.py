n = int(input())

for numbers in range(n):
    current_num = int(input())

    if current_num % 2 != 0:
        print(f"{current_num} is odd!")
        break

else:
    print(f"All numbers are even.")