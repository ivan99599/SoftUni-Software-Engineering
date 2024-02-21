
def char_range(start, stop):
    output_list = []
    for index in range(ord(start) + 1, ord(stop)):
        output_list.append(chr(index))
    output = " ".join(output_list)
    return output


char_start = input()
char_end = input()
print(char_range(char_start, char_end))