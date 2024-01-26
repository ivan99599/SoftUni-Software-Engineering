n = int(input())
word = input()
list_with_all = []
filtered_list = []
for number in range(n):
    current_string = input()
    list_with_all.append(current_string)
    if word in current_string:
        filtered_list.append(current_string)

print(list_with_all)
print(filtered_list)