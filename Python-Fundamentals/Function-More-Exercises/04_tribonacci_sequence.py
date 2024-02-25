def tribonacci(n):
    tribonacci_sequence = [1, 1, 2]

    for _ in range(3, n):
        next_number = sum(tribonacci_sequence[-3:])
        tribonacci_sequence.append(next_number)

    return tribonacci_sequence[:n]

# Example usage
number = int(input())
result = tribonacci(number)
print(" ".join(map(str, result)))