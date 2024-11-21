import os

# Create and write to a file
try:
    with open('devtools_1.txt', 'w') as file:
        file.write('\nHello, world!')
    print("File written successfully")
except IOError as e:
    print(f"File operation failed: {e}")

# Read from the file
try:
    with open('devtools_1.txt', 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except IOError as e:
    print(f"File operation failed: {e}")

# Create a directory
try:
    os.mkdir('new_directory')
    print("Directory created successfully")
except OSError as e:
    print(f"Directory creation failed: {e}")

# Change current working directory
try:
    os.chdir('new_directory')
    print(f"Changed working directory to: {os.getcwd()}")
except OSError as e:
    print(f"Changing directory failed: {e}")

# List files in the current directory
try:
    files = os.listdir('.')
    print("Files in directory:")
    print(files)
except OSError as e:
    print(f"Listing directory contents failed: {e}")

# Define and raise a custom exception
class CustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(e.message)

# Clean up: Go back to the parent directory and remove the created directory
os.chdir('..')
try:
    os.rmdir('new_directory')
    print("Directory removed successfully")
except OSError as e:
    print(f"Directory removal failed: {e}")
