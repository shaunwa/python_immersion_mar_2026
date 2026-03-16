def get_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def print_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

print_fibonacci(10)