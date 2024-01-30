import sys
list_of_integers = [int(num) for num in input().split()]
n = int(input())
smallest_num = sys.maxsize
for numbers in range(n):
    for current_number in list_of_integers:
        if current_number < smallest_num:
            smallest_num = current_number
    if smallest_num in list_of_integers:
        list_of_integers.remove(smallest_num)
    smallest_num = sys.maxsize

formatted_integers = ", ".join(map(str, list_of_integers))
print(formatted_integers)import sys
list_of_integers = [int(num) for num in input().split()]
n = int(input())
smallest_num = sys.maxsize
for numbers in range(n):
    for current_number in list_of_integers:
        if current_number < smallest_num:
            smallest_num = current_number
    if smallest_num in list_of_integers:
        list_of_integers.remove(smallest_num)
    smallest_num = sys.maxsize

formatted_integers = ", ".join(map(str, list_of_integers))
print(formatted_integers)
