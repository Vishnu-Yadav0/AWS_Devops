'''

Python try...except Block

The try...except block is used to handle exceptions in Python.

try:
    # code that may cause exception
except:
    # code to run when exception occurs
'''


try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

# Output: Error: Denominator cannot be 0. 