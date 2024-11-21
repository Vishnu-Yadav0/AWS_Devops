class Computer1:
    def __init__(self, cpu, ram): # Special Methods are __init__   Note: init stands for initialise the variables 
        self.cpu = cpu
        self.ram = ram 

    def config(self):          # Variables : 1. Special Variables __name__ and Special Methods are __init__         
        print("System Configuration is: ", self.cpu, self.ram) # Computer : 1. CPU, 2. RAM, 3. Hard Disk 

# Create a Object and Call a Function
object12 = Computer1('i5','8gb')
# object23 = Computer1('i3','4gb')

object12.config()
# object23.config()


class Dog:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

# Creating instances with and without parameters
dog1 = Dog("Rocky", 6)
dog2 = Dog()

print(dog1.name)  # Output: Buddy
print(dog1.age)

print(dog2.name)  # Output: Unknown

print(id(dog1))

print(id(dog2))