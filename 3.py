# создайте функцию - генератор чисел Фибоначчи.

def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

data = list(fibonacci(15))
print(data)
