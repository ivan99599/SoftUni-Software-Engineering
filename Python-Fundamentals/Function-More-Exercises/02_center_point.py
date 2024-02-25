import math

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

def closest_to_center(x1, y1, x2, y2):
    distance1 = (x1 ** 2) + (y1 ** 2)
    distance2 = (x2 ** 2) + (y2 ** 2)
    if distance1 > distance2:
        return print(f"({math.floor(x2)}, {math.floor(y2)})")
    else:
        return print(f"({math.floor(x1)}, {math.floor(y1)})")


closest_to_center(a1, b1, a2, b2)