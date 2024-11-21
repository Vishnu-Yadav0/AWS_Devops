# Python Syntax

print("Welcome To Cloud Binary!")

# Single Line Comments

''' 
Single Triple
multiline docstring
'''

"""
Double Triple
multiline docstring.
"""

# Python Variables
x = 5
y = "Cloud Binary"
print(x)
print(y)

# Output Both Text and a Variable
x = "AWS"
y = "And"
z = "DevOps"
print(x, y, z)

# Add a Variable To Another Variable
x = "AWS "
y = "And "
z = "DevOps"
print(x + y + z)

# Python Numbers
'''
There are three numeric types in Python:

int
float
complex
'''
# Verify the Type of An Object - Variables of numeric types are created when you assign a value to them:
x = 1
y = 2.8
z = 1j

# To verify the type of any object in Python, use the type() function:

print(type(x))
print(type(y))
print(type(z))

'''
Int
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
'''
# Create Integers
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

'''
Float
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

'''
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

"""
Complex
Complex numbers are written with a "j" as the imaginary part:
"""
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

'''
Type Conversion

You can convert from one type to another with the int(), float(), and complex() methods:

'''
# Convert from one type to another:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

'''
Random Number

Python does not have a random() function to make a random number, 
but Python has a built-in module called random that can be used to make random numbers:

'''
# Import the random module, and display a random number between 1 and 9:
import random

print(random.randrange(1, 10))

# Python Casting

'''
Specify a Variable Type

There may be times when you want to specify a type on to a variable. 

This can be done with casting. 

Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)

float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)

str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

'''
# Integers:
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

print(x)
print(y)
print(z)

# Floats:
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

print(x)
print(y)
print(z)
print(w)

# Strings:
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

print(x)
print(y)
print(z)

# Python Strings

'''
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:

'''
print("------------------------------------------------")
x = 'AWS'
y = "And"
z = "DevOps"
print(x, y, z)

'''
Quotes Inside Quotes
You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
'''

print("------------------------------------------------")

print("It's DevOps Engineer Role")
print("He is called 'DevSecOps Engineer'")
print('He is called "FinOps Engineer"')

'''
Assign String to a Variable

Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

'''
print("------------------------------------------------")
a = "DevOps"
print(a)

'''
Multiline Strings

You can assign a multiline string to a variable by using three quotes:

'''

whatiscloudcomputing = """Cloud computing is the on-demand delivery of IT resources 
over the Internet with pay-as-you-go pricing. 
Instead of buying, owning, and maintaining physical data centers and servers, 
you can access technology services, such as computing power, 
storage, and databases, 
on an as-needed basis from a cloud provider like Amazon Web Services (AWS)."""

print("------------------------------------------------")
print(whatiscloudcomputing)

whatisdevops = '''DevOps is the combination of cultural philosophies, practices, and 
tools that increases an organization’s ability to deliver applications and services 
at high velocity: evolving and improving products at a 
faster pace than organizations using traditional software development and 
infrastructure management processes. This speed enables organizations to better 
serve their customers and compete more effectively in the market.'''

print("------------------------------------------------")
print(whatisdevops)

'''
Strings are Arrays

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
'''

# Get the character at position 1 (remember that the first character has the position 0):

a = "DevOps is the combination of cultural philosophies, practices, and tools"
print(a[1])

'''
Looping Through a String

Since strings are arrays, we can loop through the characters in a string, with a for loop.
'''

for i in a:
    print(i)

'''
String Length
To get the length of a string, use the len() function.
'''

# The len() function returns the length of a string:

a = "DevOps is the combination of cultural philosophies, practices, and tools"
print(len(a))

'''
Check String

To check if a certain phrase or character is present in a string, we can use the keyword in.

'''

# Check if "free" is present in the following text:

txt = "DevOps is the combination of cultural philosophies, practices, and tools"
print("cultural" in txt)

'''
Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
'''
print("cultural" not in txt)

# Use it in an if statement:

txt = "DevOps is the combination of cultural philosophies, practices, and tools"

if "tools" in txt:
    print("Yes 'tools' is present")

txt = "DevOps is the combination of cultural philosophies, practices, and tools"

if "Cloudbinary" not in txt:
    print("No 'Cloudbinary' Exists")

# Python Operators

'''
Python Operators

Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:

Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators

'''
# Arithmetic operators:
'''
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y	
'''

# Python Assignment Operators

'''Assignment operators are used to assign values to variables:


Operator	Example	    Same As	
=	        x = 5	    x = 5	
+=	        x += 3	    x = x + 3	
-=	        x -= 3	    x = x - 3	
*=	        x *= 3	    x = x * 3	
/=	        x /= 3	    x = x / 3	
%=	        x %= 3	    x = x % 3	
//=	        x //= 3	    x = x // 3	
**=	        x **= 3	    x = x ** 3	
&=	        x &= 3	    x = x & 3	
|=	        x |= 3	    x = x | 3	
^=	        x ^= 3	    x = x ^ 3	
>>=	        x >>= 3	    x = x >> 3	
<<=	        x <<= 3	    x = x << 3	
:=	        print(x := 3)	    x = 3 print(x)
'''

# Python Comparison Operators
'''
Comparison operators are used to compare two values:

==	Equal	                    x == y	
!=	Not equal	                x != y	
>	Greater than	            x > y	
<	Less than	                x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	    x <= y

'''

# Python Logical Operators
'''
Logical operators are used to combine conditional statements:

and 	Returns True if both statements are true	                x < 5 and  x < 10	
or	    Returns True if one of the statements is true	            x < 5 or x < 4	
not	    Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)
'''

# Python Identity Operators
'''
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:


is 	    Returns True if both variables are the same object	        x is y	
is not	Returns True if both variables are not the same object	    x is not y
'''

# Python Membership Operators

'''
Membership operators are used to test if a sequence is presented in an object:

in 	    Returns True if a sequence with the specified value is present in the object	   x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y
'''

# Python Bitwise Operators

'''
Bitwise operators are used to compare (binary) numbers:

& 	    AND	                    Sets each bit to 1 if both bits are 1	                x & y	
|	    OR	                    Sets each bit to 1 if one of two bits is 1	            x | y	
^	    XOR	                    Sets each bit to 1 if only one of two bits is 1	        x ^ y	
~	    NOT	                    Inverts all the bits	                                   ~x	
<<	    Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	    Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2

'''

# Operator Precedence
'''
Operator precedence describes the order in which operations are performed.

Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
'''

print((6 + 3) - (6 + 3))

# Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:

print(100 + 5 * 3)

# The precedence order is described in the table below, starting with the highest precedence at the top:
'''

()	                Parentheses	
**	                Exponentiation	
+x  -x  ~x	        Unary plus, unary minus, and bitwise NOT	
*  /  //  %	        Multiplication, division, floor division, and modulus	
+  -	            Addition and subtraction	
<<  >>	            Bitwise left and right shifts	
&	                Bitwise AND	
^	                Bitwise XOR	
|	                Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not             	Logical NOT	
and	                AND	
or	                OR

If two operators have the same precedence, the expression is evaluated from left to right.

'''

# Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:

print(5 + 4 - 7 + 3)


# Python Lists

mylist = ["DevOps", "FinOps", "DevSecOps"]

'''
List

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
'''

thislist = ["DevOps", "FinOps", "DevSecOps"]
print(thislist)

'''
List Items

List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.
'''

'''
Ordered

When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.
'''

'''
Changeable

The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Allow Duplicates

Since lists are indexed, lists can have items with the same value:

'''
thislist = ["FinOps", "DevSecOps", "DevOps", "FinOps", "DevSecOps"]
print(thislist)

'''
List Length

To determine how many items a list has, use the len() function:
'''
thislist = ["FinOps", "DevSecOps", "DevOps", "FinOps", "DevSecOps"]
print(len(thislist))

'''
List Items - Data Types

List items can be of any data type:
'''

list1 = ["FinOps", "DevSecOps",'AIOps']
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

# A list can contain different data types:
# A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]
print(list1)

'''
type()

From Python's perspective, lists are defined as objects with the data type 'list':

<class 'list'>
'''
print(type(list1))

'''
The list() Constructor

It is also possible to use the list() constructor when creating a new list.
'''
# Using the list() constructor to make a List:
thislist = list(("FinOps", "DevSecOps",'AIOps')) # note the double round-brackets
print(thislist)

'''
Python Collections (Arrays)

There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.

Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

Dictionary is a collection which is ordered** and changeable. No duplicate members.


*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

'''

# Python Tuples

mytuple = ("apple", "banana", "cherry")

'''
Tuple

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
'''

# Create a Tuple:

thistuple = ("apple", "banana", "cherry")

print(thistuple)

'''
Tuple Items

Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:
'''

# Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

'''
Tuple Length

To determine how many items a tuple has, use the len() function:
'''

# Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

'''
Create Tuple With One Item

To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
'''

# One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

'''
Tuple Items - Data Types

Tuple items can be of any data type:
'''

# String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple can contain different data types:

# A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")


'''
type()

From Python's perspective, tuples are defined as objects with the data type 'tuple':

<class 'tuple'>
'''
# What is the data type of a tuple?

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

'''
The tuple() Constructor

It is also possible to use the tuple() constructor to make a tuple.

'''
# Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


'''
Python Collections (Arrays)

There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.

Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

'''

'''
Python Sets

Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.

'''

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

'''
Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.

Duplicates Not Allowed
Sets cannot have two items with the same value.

'''
# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

{'cherry', 'banana', 'apple'}

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

{True, 2, 'banana', 'cherry', 'apple'}

# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

# False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

{False, True, 'apple', 'cherry', 'banana'}

'''
Get the Length of a Set
To determine how many items a set has, use the len() function.

Example
Get the number of items in a set:

'''
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

'''
Set Items - Data Types
Set items can be of any data type:

Example
String, int and boolean data types:

'''

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

{'cherry', 'apple', 'banana'}
{1, 3, 5, 7, 9}
{False, True}

# A set can contain different data types:

# A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}

'''
type()
From Python's perspective, sets are defined as objects with the data type 'set':

<class 'set'>

'''

# What is the data type of a set?

myset = {"apple", "banana", "cherry"}
print(type(myset))


'''
The set() Constructor
It is also possible to use the set() constructor to make a set.

Example
Using the set() constructor to make a set:
'''

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

'''

Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove items and add new items.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

'''

'''
Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values:

'''

aws = {

    "ec2": "Virtual Machines",
    "ec2_year": 2006,
    "s3": "Simple Storage Service",
    "s3_year": 2006.07, 
    "route53": "DNS",
    "iaas": "true"
}

print(aws)