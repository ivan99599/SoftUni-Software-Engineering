number = int(input())

def perfect_num(current_number):
    list_of_numbers = []
    for num in range(1, current_number + 1):
        if current_number % num == 0 and num != current_number:
            list_of_numbers.append(num)
    if sum(list_of_numbers) == current_number:
        return "We have a perfect number!"
    return "It's not so perfect."


result = perfect_num(number)
print(result)