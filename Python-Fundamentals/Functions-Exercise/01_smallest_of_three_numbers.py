def smallest_num(first_num, second_num, third_num):
    if second_num > first_num < third_num:
        return first_num
    elif first_num > second_num < third_num:
        return second_num
    elif second_num > third_num < second_num:
        return third_num


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(smallest_num(first_number, second_number, third_number))
