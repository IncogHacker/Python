


 
class division:

    def __init__(obj,value):

        obj.value=value
        

    
    def __truediv__(obj1,obj2):

        return  obj1.value/obj2.value
        








obj1=division(5)
obj2=division(10)

print(obj1/obj2)