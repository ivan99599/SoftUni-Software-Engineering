
while True:
    current_string = input()
    if current_string == "end":
        break
    reverse_word = current_string[::-1]
    print(f"{current_string} = {reverse_word}")

