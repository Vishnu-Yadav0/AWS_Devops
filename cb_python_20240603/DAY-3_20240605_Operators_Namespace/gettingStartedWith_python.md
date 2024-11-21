#### Session Video

```
https://drive.google.com/file/d/1VsfGOW-ZEHMELIWNRwkIN2J6ospovm2N/view?usp=sharing
```

#### Python Module-1

```

1. Getting Started with Python

2. Keywords and Identifiers

3. Statements & Comments

4. Python Variables

5. Python Datatypes

6. Python Type Conversion

7. Python I/O and import

8. Python Operators

9. Python Namespace

```

#### 2. Keywords and Identifiers

```
Keywords are reserved words in Python that have special meanings. You cannot use them as identifiers (names for variables, functions, etc.). Examples include False, True, None, and, or, not, if, else, elif, while, for, def, return, import, from, as, class, try, except, raise, and finally.

# List of some Python keywords

import keyword
print(keyword.kwlist)

Identifiers are names used to identify a variable, function, class, module, or other objects. They can contain letters (a-z, A-Z), digits (0-9), and underscores (_). They must start with a letter or an underscore but cannot start with a digit. Identifiers are case-sensitive.


# Valid identifiers
my_var = 10
_my_var = 20
myVar2 = 30

# Invalid identifiers
# 2myvar = 40  # cannot start with a digit
# my-var = 50  # cannot contain hyphen
# my var = 60  # cannot contain space

```

#### 3. Statements & Comments

```
Statements are instructions that a Python interpreter can execute. Examples include assignments, function calls, and control flow statements.


# Assignment statement
x = 5

# Function call statement
print(x)

# Control flow statement
if x > 0:
    print("x is positive")


Comments are non-executable parts of the code used to explain the code. Single-line comments start with #. Multi-line comments can be created using triple quotes ''' or """.


# This is a single-line comment

"""
This is a multi-line comment
spanning multiple lines.
"""

'''
Another way to create
a multi-line comment.
'''



```

#### 4. Python Variables

```
Variables are containers for storing data values. You do not need to declare them before use, and their data type can change during runtime.

# Assigning values to variables
a = 10
b = "Hello"
c = 3.14

# Reassigning different types to the same variable
a = "Python"

```


