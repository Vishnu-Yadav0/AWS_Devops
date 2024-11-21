# 1. Getting Command-line Arguments

import sys

# Print command line arguments
# print("Script name:", sys.argv[0])

# for i in range(1, len(sys.argv)):
#     print(f"Argument {i}: {sys.argv[i]}")

# 2. Exiting the Script
# import sys

# print("Exiting the script")
# sys.exit(0)

# 3. Reading from Standard Input
# import sys

# print("Enter something: ")
# input_text = sys.stdin.readline().strip()
# print(f"You entered: {input_text}")

# 4. Writing to Standard Output
# import sys

# sys.stdout.write("This is standard output\n")

# 5. Writing to Standard Error
# import sys

# sys.stderr.write("This is standard error\n")

# 6. Getting the Python Version
# import sys

# print("Python version:", sys.version)

# 7. Getting the Python Version Info
# import sys

# print("Python version info:", sys.version_info)

# 8. Getting the Platform Information
# import sys

# print("Platform:", sys.platform)

# 9. Getting the Path of the Python Interpreter

# import sys

# print("Python executable:", sys.executable)

# 10. Getting the List of Module Search Paths
# import sys

# print("Module search paths:", sys.path)

# 11. Adding a New Path to the Module Search Paths
# import sys

# new_path = '/path/to/directory'
# sys.path.append(new_path)
# print("Updated module search paths:", sys.path)

# 12. Getting the Maximum Recursion Limit
# import sys

# print("Maximum recursion limit:", sys.getrecursionlimit())

# 13. Setting a New Recursion Limit
# import sys

# sys.setrecursionlimit(1500)
# print("New recursion limit:", sys.getrecursionlimit())

# 14. Getting the Size of an Object in Bytes
# import sys

# obj = "Hello, World!"
# print(f"Size of the object in bytes: {sys.getsizeof(obj)}")

# 15. Getting the Reference Count of an Object
# import sys

# obj = []
# print(f"Reference count of the object: {sys.getrefcount(obj)}")

# 16. Getting the Default Encoding
# import sys

# print("Default encoding:", sys.getdefaultencoding())

# 17. Getting the File System Encoding
# import sys

# print("File system encoding:", sys.getfilesystemencoding())

# 18. Getting the Current Frame
# import sys

# frame = sys._getframe()
# print("Current frame:", frame)

# 19. Getting the Current Module
# import sys

# module = sys.modules[__name__]
# print("Current module:", module)

# 20. Printing the List of Loaded Modules
# import sys

# print("Loaded modules:")
# for module_name in sys.modules:
#     print(module_name)
