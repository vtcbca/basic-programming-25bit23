def is_prime_recursive(n, divisor=None):
    if n <= 1:
        return False
    if divisor is None:
        divisor = int(n**0.5)
    if divisor < 2:
        return True
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor - 1)

# Example usage
number = int(input("Enter a number: "))
print(f"{number} is prime: {is_prime_recursive(number)}")
