first_string = input()
second = input()


while first_string in second:
    second = second.replace(first_string, "")

print(second)


