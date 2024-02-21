numbers = [digit for digit in input().split(", ")]


def palindrome_check(nums_string):
    for num in numbers:
        print(num == num[::-1])


palindrome_check(numbers)
