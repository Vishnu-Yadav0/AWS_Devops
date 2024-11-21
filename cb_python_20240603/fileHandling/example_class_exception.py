# Creating and using a user-defined exception:

# Defining a user-defined exception
class CustomError(Exception):
    def __init__(self, message):
        self.message = message

# Using the user-defined exception
try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(e.message)
