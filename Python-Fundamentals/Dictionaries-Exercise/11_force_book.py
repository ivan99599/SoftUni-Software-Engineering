force_book = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if "|" in command:
        command_with_pipe = command.split(" | ")
        force_side = command_with_pipe[0]
        force_user = command_with_pipe[1]
        user_is_part_of_the_force = False
        for value in force_book.values():
            user_is_part_of_the_force = True
            break
        if force_user not in force_book:
            if force_side not in force_book:
                force_book[force_side] = []
            force_book[force_side].append(force_user)
    if "->" in command:
        command_with_arrow = command.split(" -> ")
        force_user = command_with_arrow[0]
        force_side = command_with_arrow[1]
        for value in force_book.values():
            if force_user in value:
                value.remove(force_user)
                break

