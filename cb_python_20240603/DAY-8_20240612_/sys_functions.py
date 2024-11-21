import sys   

def sys_info():
    info = {}

    # Command-line arguments
    info['argv'] = sys.argv
    
    # Python version
    info['version'] = sys.version
    
    # Python version info
    info['version_info'] = sys.version_info
    
    # Platform
    info['platform'] = sys.platform
    
    # Python executable path
    info['executable'] = sys.executable
    
    # Module search paths
    info['path'] = sys.path
    
    # Maximum recursion limit
    info['recursion_limit'] = sys.getrecursionlimit()
    
    # Default encoding
    info['default_encoding'] = sys.getdefaultencoding()
    
    # File system encoding
    info['filesystem_encoding'] = sys.getfilesystemencoding()
    
    # Current frame
    info['current_frame'] = sys._getframe()
    
    # Loaded modules
    info['loaded_modules'] = list(sys.modules.keys())

    return info

import pprint 
info = sys_info()

#pprint.pprint(info)


# Accessing Specific Information
# Get system information
info = sys_info()

# Print command-line arguments
print("Command-line arguments:", info['argv'])

# Print Python version
print("Python version:", info['version'])

# Print platform
print("Platform:", info['platform'])

# Print module search paths
print("Module search paths:", info['path'])

# Print loaded modules
print("Loaded modules:", info['loaded_modules'])

# Handling Command-line Arguments
def handle_args():
    info = sys_info()
    args = info['argv']
    
    if len(args) < 2:
        print("No command-line arguments provided.")
    else:
        for i, arg in enumerate(args[1:], start=1):
            print(f"Argument {i}: {arg}")

# Call the function to handle command-line arguments
handle_args()

# Changing Recursion Limit and Checking Size of an Object
def check_recursion_limit_and_size():
    info = sys_info()
    
    # Print the current recursion limit
    print("Current recursion limit:", info['recursion_limit'])
    
    # Set a new recursion limit
    sys.setrecursionlimit(2000)
    print("New recursion limit:", sys.getrecursionlimit())
    
    # Check the size of a sample object
    sample_obj = "Hello, World!"
    print(f"Size of the object '{sample_obj}': {sys.getsizeof(sample_obj)} bytes")

# Call the function
check_recursion_limit_and_size()

# Printing Python and File System Encodings

def print_encodings():
    info = sys_info()
    
    # Print default encoding
    print("Default encoding:", info['default_encoding'])
    
    # Print file system encoding
    print("File system encoding:", info['filesystem_encoding'])

# Call the function
print_encodings()


'''
Explanation
sys_info Function:
This function gathers various pieces of information using the sys module and returns them in a dictionary.
Example 1:
Demonstrates how to retrieve and pretty print the entire system information.
Example 2:
Shows how to access specific pieces of information from the dictionary returned by sys_info.
Example 3:
Handles and prints command-line arguments.
Example 4:
Changes the recursion limit and checks the size of an object in bytes.
Example 5:
Prints the default encoding and file system encoding.
These examples should help you understand how to use the sys module effectively in different scenarios.
'''