

# here We inherit from parent class then make another class from child .. or we can say when a child class become parents for another class


class parent1:
        comapny="Infotech"
        def __init__(self):
         print(self.comapny)
    
class child1(parent1):
     comapny="No info tech"
     
     def __init__(self):
          pass   # if a child class has its own __init__, Python does NOT call the parent’s __init__ automatically.

class child2(child1):
     pass

obj=child1()
obj2=child2()

print(obj.comapny)
print(obj2.comapny)
    



