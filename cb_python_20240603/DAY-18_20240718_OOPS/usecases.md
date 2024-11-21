# Session Video:

```
https://drive.google.com/file/d/1CK3XmppC5D52aA82xH-xttPg9MN71nvR/view?usp=sharing
```

#### Python OOPS

```

### We have explored to python fundamentals:


1. Variables
2. Functions
3. Module
4. Packages

Why python is unique?

Python supports all three programming paradigms
    1. Functional Programming
    2. Object Oriented Programming
    3. Procedure Oriented Programming


### 1. Functional Programming

Functional programming is a paradigm that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data. 

Python supports functional programming features like higher-order functions, first-class functions, anonymous functions (lambdas), and functions from the functools module.


# Using a lambda function
double = lambda x: x * 2
print(double(5))  # Output: 10

# Higher-order function: map
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(double, numbers))
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]

# Using functools.reduce
from functools import reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15


# 2. Object-Oriented Programming

As discussed earlier, Python fully supports OOP, allowing the definition of classes and objects, inheritance, encapsulation, polymorphism, and more.


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

dog = Dog("Buddy", 9)
print(dog.bark())  # Output: Buddy says Woof!


# 3. Procedural Programming

Procedural programming is a paradigm derived from structured programming, based on the concept of procedure calls, 
where procedures (also known as routines, subroutines, or functions) are used to perform tasks. 

Python supports this through its rich set of built-in functions and the ability to define user-defined functions.


def add(a, b):
    return a + b

def main():
    num1 = 10
    num2 = 20
    result = add(num1, num2)
    print(f"The sum is: {result}")

if __name__ == "__main__":
    main()  # Output: The sum is: 30



# Conclusion
Python is a versatile language that supports multiple programming paradigms, including functional programming, 
object-oriented programming, and procedural programming. 

This flexibility allows developers to choose the best paradigm for their specific use case or even combine 
paradigms within a single project.

#### Python OOPS

Object-Oriented Programming (OOP) in Python is a programming paradigm that uses objects and classes to structure and manage code.

Classes and Objects :

1. Class: A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.

2. Object: An instance of a class. It contains the data and the methods defined by its class.


class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Dog class
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

print(buddy.name)  # Output: Buddy
print(miles.age)   # Output: 4


```

