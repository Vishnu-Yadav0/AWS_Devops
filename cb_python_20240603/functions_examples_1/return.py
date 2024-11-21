# The return Statement

# We return a value from the function using the return statement
# Note: The return statement also denotes that the function has ended. Any code after return is not executed.

# Create a Function
def find_value(a):
    result = a * a 
    return result

# Calling a Function
b = find_value(3)

print("Value: ", b)

