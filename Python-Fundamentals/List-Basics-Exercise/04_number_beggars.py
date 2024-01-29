money_as_integers = [int(num) for num in input().split(", ")]
count_of_beggars = int(input())
final_sums = []
start_index = 0
while start_index < count_of_beggars:
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_as_integers), count_of_beggars):
        current_beggar_sum += money_as_integers[current_index]
    final_sums.append(current_beggar_sum)
    start_index += 1

print(final_sums)