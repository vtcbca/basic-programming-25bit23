def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example: Generate first 10 Fibonacci numbers
gen = fibonacci_generator()
print([next(gen) for _ in range(10)])

# Example: Generate Fibonacci numbers less than 50
gen = fibonacci_generator()
fib_less_50 = []
for num in gen:
    if num >= 50:
        break
    fib_less_50.append(num)
print(fib_less_50)
