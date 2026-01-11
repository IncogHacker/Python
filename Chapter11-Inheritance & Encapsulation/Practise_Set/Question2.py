


#  Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’


class Animals:


    def __init__(self):
        pass

    @ property
    def _animal(self):
        return f"Animal"


class Pet(Animals):
    def __init__(self):
        pass

    @property
    def _callPet(self):        
        return f"This  is Pet Class"


class Dog(Pet):

    @staticmethod  # @staticmethod is a decorator that defines a method inside a class which does not use self or cls and call through simple function.

    def bark():
        
        print("Dog Barking Started")



obj=Animals()

obj2=Dog()

obj3=Pet()

print(obj3._callPet)

print(obj3._animal)




obj2.bark()


