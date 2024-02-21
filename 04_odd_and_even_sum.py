def odd_sum(number):
    odd_num = 0
    for current_num in number:
        num = int(current_num)
        if num % 2 != 0:
            odd_num += num
    return odd_num

def even_sum(number):
    even_num = 0
    for current_num in number:
        num = int(current_num)
        if num % 2 == 0:
            even_num += num
    return even_num


digit = input()
result_1 = odd_sum(digit)
result_2 = even_sum(digit)
print(f"Odd sum = {result_1}, Even sum = {result_2}")