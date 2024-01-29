cards = input().split()
count_of_shuffles = int(input())
for shuffle in range(count_of_shuffles):
    middle_of_deck = len(cards) // 2
    left_half = cards[0:middle_of_deck]
    right_half = cards[middle_of_deck:]
    deck_after_shuffling = []
    for card_index in range(len(left_half)):
        deck_after_shuffling.append(left_half[card_index])
        deck_after_shuffling.append(right_half[card_index])
    cards = deck_after_shuffling

print(cards)
