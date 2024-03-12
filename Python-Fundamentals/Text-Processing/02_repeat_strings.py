sequence_of_string = input().split()
new_string = ""
for char in sequence_of_string:
    new_string += char * len(char)

print(new_string)