def even_number(some_numbers):
    even_list = []
    for number in some_numbers:
        number = int(number)
        if number % 2 == 0:
            even_list.append(number)
    return even_list


numbers = input().split()
result = even_number(numbers)
print(result)