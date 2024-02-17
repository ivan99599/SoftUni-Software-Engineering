# def repeat(current_string, number):
#     return current_string * number
#
#
# some_string = input()
# n = int(input())
# print(repeat(some_string, n))


some_string = input()
n = int(input())

repeating_string = lambda a, b: a * b
result = repeating_string(some_string, n)
print(result)