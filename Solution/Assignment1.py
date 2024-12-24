from functools import reduce

def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

# Example usage
number = 5
print(f"Factorial of {number} is {factorial_reduce(number)}")
