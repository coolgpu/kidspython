def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
        print(value)
        return value


x = 10

print('The %dth fibonacci number is %d' % (x, fibonacci(x)))