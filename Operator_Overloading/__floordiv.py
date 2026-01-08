
#Decimal removed like if we have 3.6 it result 3 lower value



class floor_method:

    def __init__(self,value):
        self.value=value

        


    
    def __floordiv__(one,two):

        return  one.value//two.value

        
        







obj1=floor_method(int(input("Enter The number")))
obj2=floor_method(int(input("Enter The number")))


print(obj1//obj2)