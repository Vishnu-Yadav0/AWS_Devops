
'''

Type conversion refers to converting one data type to another. 

It can be done using built-in functions like int(), float(), str(), list(), tuple(), set(), dict(), etc.

'''
# Implicit type conversion
num_int = 123
num_float = 1.23
num_new = num_int + num_float  # num_new is automatically converted to float

# Explicit type conversion
# num_str = "456"
# num_int = int(num_str)
# num_float = float(num_str)

print(num_int, type(num_int))
print(num_float, type(num_float))
print(num_new, type(num_new))

# print(num_str, type(num_str))
# print(num_int, type(num_int))
# print(num_float, type(num_float))
