"""
Python break and continue

break is used to exit a loop prematurely.

continue is used to skip the rest of the code inside the loop for the current iteration and move to the next iteration.
"""
# break Example:

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

'''
0 == 5 = 0
1 == 5 = 1
2 == 5 = 2
3 == 5 = 3
4 == 5 = 4
5 == 5 = 5
'''

# continue Example:

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

'''
Python Pass
The pass statement is a null operation; nothing happens when it executes. It's used as a placeholder in loops, functions, classes, or conditionals.

'''

for i in range(5):
    if i == 3:
        pass  # Do nothing (placeholder)
    else:
        print(i)

"""
Differences Between Pass and Continue in Python
A pass statement signals to a loop that there is “no code to execute here.” It's a placeholder for future code. 

A continue statement is used to force the loop to skip the remaining code and start the next iteration.

"""

def my_function():
    pass  # Will be implemented later

class MyClass:
    pass  # Will be implemented later

"""

# Summary

if...else: Used for conditional execution.

for loop: Used for iterating over a sequence.

while loop: Repeats code while a condition is True.

break: Exits the loop prematurely.

continue: Skips the current iteration and continues with the next.

pass: Null operation used as a placeholder.

"""