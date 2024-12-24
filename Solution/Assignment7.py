n = int(input("Enter the number of lines: "))

# Precompute all rows
pattern = []
for i in range(1, n + 1):
    row = " ".join(str(j) for j in range(1, 2 * i))
    pattern.append(" " * (n - i) + row)

# Print the pattern
print("\n".join(pattern))
