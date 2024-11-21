# 6. Membership Operators: in, not in

# in 
# Checks if a value is present in a sequence (such as a list, tuple, string, etc.).

# Example with a list
numbers = [1, 2, 3, 4, 5]
value = 3
result = value in numbers
print(f"{value} in {numbers}: {result}")

# Example with a string
string = "Hello, world!"
substring = "world"
result = substring in string
print(f'"{substring}" in "{string}": {result}')

# 2. not in
# Checks if a value is not present in a sequence.

# Example with a list
numbers = [1, 2, 3, 4, 5]
value = 6
result = value not in numbers
print(f"{value} not in {numbers}: {result}")

# Example with a string
string = "Hello, world!"
substring = "Python"
result = substring not in string
print(f'"{substring}" not in "{string}": {result}')
