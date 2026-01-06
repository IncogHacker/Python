

# here as we know when we define function then some function do not need the parameter or self paraneter so we use @staticmethod

# !🔹 Why do we need static method?

# Use it when:

# method does not need object data-- means no need to create a object

# method does not need class data

# logic is related to the class conceptually




class cars:
    
    @staticmethod  # Here We dont Need to give parameter like self  also static method is decorator
    # getinfo=@staticmethod(getinfo)
    # It returns a descriptor object that tells Python:
    # “Do NOT bind this function to an instance attribute or variable so without object creation it work”
    
    def getinfo(a,b):

        return a+b  #! It returns to the PLACE where getinfo() was CALLED
        



    
print(cars.getinfo(3,4))

obj=cars()






