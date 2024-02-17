def calculations(current_operator, num1, num2):
    if current_operator == "multiply":
        return num1 * num2
    elif current_operator == "divide":
        return num1 // num2
    elif current_operator == "add":
        return num1 + num2
    elif current_operator == "subtract":
        return num1 - num2


operator = input()
first_number = int(input())
second_number = int(input())
result = calculations(operator, first_number, second_number)
print(result)