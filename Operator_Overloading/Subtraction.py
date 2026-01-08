

class operator_subtra:

    def __init__(self,value):

        self.value=value
        print(self.value)

    def __sub__(self,self2):
        
        return self.value-self2.value






obj1=operator_subtra(10)
obj2=operator_subtra(20)

print(obj1-obj2)
