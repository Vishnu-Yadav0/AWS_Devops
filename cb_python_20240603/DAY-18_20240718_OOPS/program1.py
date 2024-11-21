# Creating a Class
class Computer:
    # ----> Attributes : Variables
    # ----> Behaviours : Methods(Functions)
    def config(self):
        print("i7, 16gb, 1TB")

# Create a Object and Call a Function
object1 = Computer()
# object2 = Computer()

# Example-1 : If you want to call a method from a specific class 
Computer.config(object1)
# Computer.config(object2)

# Example-2 : If you want to call a method from a specific class 
object1.config()
# object2.config()

# Print a Method
print(type(object1))