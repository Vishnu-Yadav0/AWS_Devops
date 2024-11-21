class Computer:
    
    def __init__(self):
        self.name = "C3Ops Technologies Private Limited"
        self.type = "DevSecOps"

    def update(self):
        self.type = "Kesav"

    def compare(self,other):
        if self.type == other.type:
            return True
        else:
            return False 

c1 = Computer()         # () is a Constructor and it will call a method of class
c2 = Computer()
c1.type = "DevSecOps"

if c1.compare(c2):
    print("They are same!")

# print(id(c1))
# print(id(c2))

# print(id(c1.name),c1.name)
# print(id(c1.type),c1.type)

# c1.update()
# print(id(c1.name),c1.name)
# print(id(c1.type),c1.type)