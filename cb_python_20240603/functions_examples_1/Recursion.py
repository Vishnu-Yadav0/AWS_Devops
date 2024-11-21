# Recursion

# Recursion is the process of defining a function that calls itself.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(2))
