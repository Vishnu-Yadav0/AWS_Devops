# 7. Identity Operators: is, is not

# 1. is
# Checks if two variables point to the same object (i.e., they have the same identity).

# Example with integers
a = 10
b = 10
result = a is b
print(f"a is b: {result}")  # Output: True

# Example with lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
result = list1 is list2
print(f"list1 is list2: {result}")  # Output: False

# Example with strings
str1 = "Hello"
str2 = "Hello"
result = str1 is str2
print(f"str1 is str2: {result}")  # Output: True

# 2. is not
# Checks if two variables do not point to the same object.

# Example with integers
a = 10
b = 20
result = a is not b
print(f"a is not b: {result}")  # Output: True

# Example with lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
result = list1 is not list2
print(f"list1 is not list2: {result}")  # Output: True

# Example with strings
str1 = "Hello"
str2 = "World"
result = str1 is not str2
print(f"str1 is not str2: {result}")  # Output: True

