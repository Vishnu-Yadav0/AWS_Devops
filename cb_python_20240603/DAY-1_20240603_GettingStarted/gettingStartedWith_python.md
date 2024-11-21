#### Session Video

```
https://drive.google.com/file/d/1UWDbeM8SfW1Iql3jyb1BQa5ibWaMDkIr/view?usp=sharing
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

#### 1. Getting Started with Python

#### What is Python?
```
Python is a high-level, interpreted, general-purpose programming language. Known for its readability and simplicity, it emphasizes code readability and allows programmers to express concepts in fewer lines of code compared to languages like C++ or Java.
```

#### Key features of Python include:

```
Easy to Learn and Use: Python has a simple syntax that mimics natural language, making it an excellent choice for beginners.

Interpreted Language: Python code is executed line-by-line, which makes debugging easier.

Cross-Platform: Python runs on various platforms, including Windows, macOS, Linux, and more.

Extensive Libraries: Python has a rich standard library and a vibrant ecosystem of third-party packages.

Community Support: Python has a large and active community, providing extensive support and resources.

```

#### History of Python

```
Late 1980s: Python was conceived by Guido van Rossum as a successor to the ABC language.

1991: The first version of Python (0.9.0) was released.

2000: Python 2.0 was released, introducing new features like list comprehensions and garbage collection.

2008: Python 3.0 was released to fix inconsistencies and remove redundancies in the language. However, it was not backward compatible with Python 2.x.

```

#### Versions of Python

```
Python has gone through several major versions, with Python 2 and Python 3 being the most significant.

Python 2.x: This series introduced many features that made Python popular but included some design flaws.
Python 3.x: This series aimed to rectify the issues found in Python 2.x, focusing on consistency and simplicity.
Python 2 reached its end of life on January 1, 2020. Python 3 is the present and future of the language, with ongoing development and support.

Some notable versions include:

Python 2.0: Introduced features like list comprehensions and garbage collection.
Python 2.7: The last release of the Python 2 series, with long-term support.
Python 3.0: Introduced new features and improvements but was not backward compatible.
Python 3.6: Introduced formatted string literals (f-strings), type hints, and other enhancements.
Python 3.7: Introduced data classes, postponed evaluation of type annotations, and more.
Python 3.8: Introduced assignment expressions (the walrus operator :=), positional-only parameters, and more.
Python 3.9: Introduced new syntax features, including union operators for dict, type hinting generics in standard collections, and more.
Python 3.10: Introduced structural pattern matching (a form of a switch-case statement).

```

#### Installation

```
To start using Python, you need to install it on your computer. You can download the latest version from the official Python website.

For Windows, macOS, and Linux:

Windows: Download the installer, run it, and follow the on-screen instructions. Ensure you check the box to add Python to your PATH.

macOS: Python 2.x is pre-installed on macOS, but you should install Python 3.x using a package manager like Homebrew (brew install python3) or by downloading the installer from the Python website.

Linux: Use your distribution's package manager (e.g., sudo apt-get install python3 for Debian-based distributions).


```
#### Running Python

```
You can run Python in various ways:

Interactive Shell: Open a terminal or command prompt and type python or python3 to enter the interactive shell.

$ python3
Python 3.x.x (default, ...) 
[GCC ...] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello, World!")
Hello, World!
>>> exit()


```
#### Script File:

```
Write your code in a .py file and run it using the Python interpreter.

$ python3 my_script.py

```
#### Integrated Development Environment (IDE)

```
Integrated Development Environment (IDE): Use an IDE like PyCharm, Visual Studio Code, or Jupyter Notebook for more advanced development features.
```

#### Python 

```
https://www.python.org/


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


