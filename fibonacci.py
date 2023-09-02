def fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1
    while len(fibonacci_series) < n:
        fibonacci_series.append(a)
        c = a +b
        a, b = b, c
    return fibonacci_series

n = int(input("Enter the number of Fibonacci length to generate: "))
answer = fibonacci(n)
print(answer)