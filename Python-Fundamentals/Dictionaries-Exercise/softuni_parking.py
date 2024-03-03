def parking_system(commands):
    registered_users = {}

    for command in commands:
        tokens = command.split()
        action = tokens[0]
        username = tokens[1]

        if action == "register":
            license_plate = tokens[2]
            if username in registered_users:
                print(f"ERROR: already registered with plate number {registered_users[username]}")
            else:
                registered_users[username] = license_plate
                print(f"{username} registered {license_plate} successfully")
        elif action == "unregister":
            if username not in registered_users:
                print(f"ERROR: user {username} not found")
            else:
                print(f"{username} unregistered successfully")
                del registered_users[username]

    for username, license_plate in registered_users.items():
        print(f"{username} => {license_plate}")


# Example usage:
n = int(input())
commands_list = [input() for _ in range(n)]
parking_system(commands_list)