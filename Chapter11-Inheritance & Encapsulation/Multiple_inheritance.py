


# Here Basically Two Parent Class and and Child inherits from two Parent classes


class Parent1_class:

    classes="Parent"
    
    def __init__(self):
        
        print(f"This is The First {self.classes} Class--")

        super().__init__()

class Parent2_class:
    classes2="Parent2"

    def __init__(self):
        
        print(f"This is The Second {self.classes2} class")

        super().__init__() # call the next class in mro order (method resolution order )

        

    # Now Making inherited class from two parents


class child(Parent1_class,Parent2_class):
    
    def __init__(self):
        print("This is The Child Class")
        super().__init__()


    # def __str__(self):
    #     return "Object of child class with multiple inheritance"    


c=child() # here we only calling child class so for printing all other classes use super().init()

# print(c) 

