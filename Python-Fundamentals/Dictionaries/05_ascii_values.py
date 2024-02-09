characters = input().split(", ")

my_dict = {character: ord(character) for character in characters}

print(my_dict)