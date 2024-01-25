number = int(input())

# First part: Increasing stars
for i in range(1, number + 1):
    for j in range(0, i):
        print("*", end="")
    print()

# Second part: Decreasing stars
for i in range(number - 1, 0, -1):
    for j in range(0, i):
        print("*", end="")
    print()