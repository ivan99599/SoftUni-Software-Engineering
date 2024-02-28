
miner_task = {}
while True:
    current_string = input()
    if current_string == "stop":
        break
    current_quantity = int(input())
    if current_string not in miner_task:
        miner_task[current_string] = 0
    miner_task[current_string] += current_quantity

for key, value in miner_task.items():
    print(f"{key} -> {value}")