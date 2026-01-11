
# Manually forcing Python to throw an exception when something is wrong or we can say custom  error made by me

# Why we raise exceptions

# To stop execution when something is wrong

# To validate input

# To create custom errors

# To handle logical mistakes clearly



class raise_error:


    def __init__(self,value1,value2):

        self.value1=value1
        self.value2=value2      

    def  Raising_error(self):

        if self.value2==0:

            #Here we raising error here to crash the program if developer doing wrong coding
            raise ZeroDivisionError("Hey Your Number is 0 Cannot Divide with zero")
        
        else:
            return self.value1/self.value2






obj=raise_error(int(input("Enter The a Number a--")),int(input("Enter The a Number b--")))

print(obj.Raising_error())


