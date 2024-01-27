numbers = [int(num) for num in input().split()]

opposite_list = []

for current_number in numbers:
    current_number = current_number * (-1)
    opposite_list.append(current_number)

print(opposite_list)