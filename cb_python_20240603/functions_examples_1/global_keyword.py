# Python Global Keyword

# The global keyword allows you to modify a global variable inside a function.

# Global Variable
x = 10

# Create a function
def modify_global():
    global x
    x = 20

# Function Call
modify_global()

# Call Global Variable
print(x)
