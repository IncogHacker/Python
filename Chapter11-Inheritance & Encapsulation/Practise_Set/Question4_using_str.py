


class complex_number:

    def __init__(self,a,b):

        self.a=a
        self.b=b

    
    def __add__(self,obj_s):

        # return f"{(self.a+obj_s.a),(self.b+obj_s.b)}"  # we can pass like this so we dont need to use __str__
         
        return complex_number((self.a+obj_s.a),(self.b+obj_s.b)) #this create a new object with different value this return the new object
    
        #  new_obj = complex_number(4, 6)
        #  complex_number.__init__(new_obj, 4, 6)
    


    def __str__(self):

        return f"{self.a,self.b}"




obj=complex_number(1, 2)
obj_s=complex_number(3, 4)


print(obj+obj_s)  # here print(new_obj,4,6) comes

# print(new_obj) calls __str__() automatically. so the real call is str(new_obj)

# !Step 1: Addition
# obj + obj_s
# → obj.__add__(obj_s)
# → returns new_obj (complex_number(4, 6))

#! Step 2: Print
# print(new_obj)

# this python automatically does 
# → print(str(new_obj))
# → new_obj.__str__()