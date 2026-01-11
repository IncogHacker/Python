



class two_d:

    def __init__(self,value1,value2):

        self.value1=value1
        self.value2=value2

        # print(self.value1)
        # print(self.value2)

    def show_two_d(self):

        return f"({self.value1},{self.value2})"
        




class three_d(two_d):

    def __init__(self,value1,value2,value3):

        super().__init__(value1,value2)  #Here Super init initialize the parent class two_d.__init__(obj2,5,3)

        # So now obj2 have there data so we dont have to write here self.value1=value1

        self.value3=value3

    
    def show_three_d(self):

        return f"({self.value1},{self.value2},{self.value3})"
        





obj1=two_d(1,2)  #two_d.__init__(obj1,1,2)

print(obj1.show_two_d())   # two_d.show_two_d(obj1)

obj2=three_d(5,3,2)

print(obj2.show_three_d())