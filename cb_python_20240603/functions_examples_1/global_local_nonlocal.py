# Global, Local, and Nonlocal

# Variables can be defined inside functions (local) or outside functions (global). 
# The nonlocal keyword is used to work with variables inside nested functions.

# Global Variable
x = "global"

def outer():
    x = "outer local"
    
    def inner():
        nonlocal x
        x = "inner local"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()
print("global:", x)
