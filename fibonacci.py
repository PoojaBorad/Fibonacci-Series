def fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1
    while len(fibonacci_series) < n:
        fibonacci_series.append(a)
        c = a + b
        a, b = b, c
    return fibonacci_series

n = 20
answer = fibonacci(n)
print(answer)