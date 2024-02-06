def fibonacci_generator(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage:
num_terms = int(input("Enter the number of terms for Fibonacci sequence: "))
fibonacci_sequence = fibonacci_generator(num_terms)
print("Fibonacci Sequence:")
print(fibonacci_sequence)
