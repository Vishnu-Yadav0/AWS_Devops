'''
__init__ is a special method used for initializing the attributes of an instance when it is created. 
It is called the constructor of the class.

Here's a breakdown of how __init__ works and what it stands for:

__init__ Method

Purpose: The __init__ method initializes the attributes of an instance.

When it is called: Automatically called when a new instance of a class is created.

Parameters: Typically takes self as its first parameter, followed by any number of additional parameters required for initialization.
'''
class Computer:

    def __init__(self): # Special Methods are __init__   Note: init stands for initialise the variables 
        print("C3Ops")

    def config(self):          # Variables : 1. Special Variables __name__ and Special Methods are __init__         
        print("i7, 16gb, 1TB") # Computer : 1. CPU, 2. RAM, 3. Hard Disk 

# Create a Object and Call a Function
object1 = Computer()
# object2 = Computer()

object1.config()
#object2.config()


class Computer1:
    def __init__(self, cpu, ram): # Special Methods are __init__   Note: init stands for initialise the variables 
        self.cpu = cpu 
        self.ram = ram 

    def config(self):          # Variables : 1. Special Variables __name__ and Special Methods are __init__         
        print("System Configuration is: ", self.cpu, self.ram) # Computer : 1. CPU, 2. RAM, 3. Hard Disk 

# Create a Object and Call a Function
object12 = Computer1('i5','8gb')
object23 = Computer1('i3','4gb')

object12.config()
object23.config()



'''
__init__ is a special method used for initializing the attributes of an instance when it is created. 
It is called the constructor of the class.

Here's a breakdown of how __init__ works and what it stands for:

__init__ Method

Purpose: The __init__ method initializes the attributes of an instance.
When it is called: Automatically called when a new instance of a class is created.
Parameters: Typically takes self as its first parameter, followed by any number of additional parameters required for initialization.
'''
class systeminfo:
    def __init__(self, cpu, ram):
        self.cpu = cpu  # Initialize the 'cpu' attribute
        self.ram = ram    # Initialize the 'ram' attribute

# Creating an instance of the systeminfo class
sysinfo = systeminfo("i7", "16 GB")

# Accessing the initialized attributes
print(sysinfo.cpu)  # Output: i7
print(sysinfo.ram)   # Output: 16 GB


'''
Key Points

Initialization: __init__ is used to initialize an instance's attributes.

Automatic Call: It is automatically invoked when a new instance of a class is created.

Customizable: You can define any number of parameters in __init__ to customize the initialization process.

Not a Constructor: While often referred to as a constructor, __init__ is technically an initializer. The actual object creation happens before __init__ is called.

Example with Default Values

You can also provide default values for parameters in __init__.
'''

class Dog:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

# Creating instances with and without parameters
dog1 = Dog("Buddy", 5)
dog2 = Dog()

print(dog1.name)  # Output: Buddy
print(dog2.name)  # Output: Unknown
print(id(dog1))
print(id(dog2))

'''
In this example, dog2 is created without providing any arguments, so it uses the default values "Unknown" 
for name and 0 for age.

In summary, __init__ is essential for setting up the initial state of an object in Python, 
making it a fundamental part of object-oriented programming in the language.

'''