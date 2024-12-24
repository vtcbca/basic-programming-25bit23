def build_row(i):
    left = [chr(65 + j) for j in range(i + 1)]
    return left + left[-2::-1]

def pattern_alphabets(n):
    for i in range(n):
        spaces = " " * (n - i - 1) * 4
        row = build_row(i)
        print(spaces + "   ".join(row))

# Example usage
pattern_alphabets(5)
