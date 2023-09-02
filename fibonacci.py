def fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1
    while len(fibonacci_series) < n:
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series

n = 20
answer = fibonacci(n)
print(answer)