command = input()
number = input()

def data_types(current_command, current_input):
    if current_command == "int":
        current_input = int(current_input) * 2
    elif current_command == "float":
        current_input = f"{float(current_input) * 1.5:.2f}"
    elif current_command == "string":
        current_input = (f"${current_input}$")
    return current_input


result = data_types(command, number)
print(result)
