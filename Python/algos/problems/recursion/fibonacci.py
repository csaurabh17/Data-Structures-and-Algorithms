# Fibonacci series up till node using recursion

# assuming node = 4, output will be [0,1,1,2,3]

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n - 2)


print(fibonacci(5))
