def plan_gifts(gifts, commands):
    gifts_list = gifts.split()

    for command in commands:
        tokens = command.split()
        action = tokens[0]

        if action == "OutOfStock":
            gift_to_remove = tokens[1]
            gifts_list = ["None" if gift == gift_to_remove else gift for gift in gifts_list]

        elif action == "Required":
            gift_to_add, index = tokens[1], int(tokens[2])
            if 0 <= index < len(gifts_list):
                gifts_list[index] = gift_to_add

        elif action == "JustInCase":
            new_gift = tokens[1]
            gifts_list[-1] = new_gift

    result = " ".join(gift for gift in gifts_list if gift != "None")
    return result


# Example usage:
gifts_input = input()
commands_input = iter(iter(input, 'No Money'))
result = plan_gifts(gifts_input, commands_input)
print(result)







