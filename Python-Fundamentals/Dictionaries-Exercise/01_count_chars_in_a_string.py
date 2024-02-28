words = input().split()
characters = {}

for word in words:
    for char in word:
        if char not in characters:
            characters[char] = 0
        characters[char] += 1

for key, value in characters.items():
    print(f"{key} -> {value}")