n = int(input())
positive = []
negative = []
count_positives = 0
for number in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive.append(current_number)
        count_positives += 1
    else:
        negative.append(current_number)

print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum(negative)}")