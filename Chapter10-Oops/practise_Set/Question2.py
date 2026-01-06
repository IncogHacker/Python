# Write a class “Calculator” capable of finding square, cube and square root of a 
# number. 

import math

class Calculator:

    def Maths(self):

        print(f"Square Root of {self.a} is {self.a**self.a}\n")
        print(f"Cube Root of {self.a} is {self.a ** 3}\n")

        # To find Sqaure root
        
        print(f"Sqaure_Root of {self.a} is {math.sqrt(self.a)}")


obj=Calculator()
obj.a=int(input("Enter The Number"))

obj.Maths()
