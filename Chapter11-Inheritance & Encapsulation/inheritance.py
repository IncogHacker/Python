

#basically if one class inherit from another class like taking variable and properties of another class call inheritance
# Inheritance shares structure (methods), NOT data
# Data must be passed explicitly

class Parent_class:
    Company="Infotech"
    pass

    def __init__(self):

        print("This is The Parent Classs")

    
class Child_class(Parent_class): # here we inherit Child_class with Parent_class so called a inherited Class
    pass
   

        
p=Parent_class()
c=Child_class()

print(p.Company)
print(c.Company)

# Here basically Child_class inherit from parent class it inherits construstor like init it also inherit class variable so it inherit every thing from parent called Inheritance 