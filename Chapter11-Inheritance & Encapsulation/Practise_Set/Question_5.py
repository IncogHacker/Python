# Write a class vector representing a vector of n dimensions. Overload the + and * 
# operator which calculates the sum and the dot(.) product of them


class Vector:

    def __init__(self,a,b,c):
        
        self.a=a
        self.b=b
        self.c=c  # here we storing these value in objects first store in v1 then v2 and then v3 


    def __add__(self,v2):
        
        #! result=self.a+v2.a+self.b+v2.b+self.c+v2.c 
        # # we can also do like this no need to make function __str__
        #! return result

        # but using str 

        result=Vector(self.a + v2.a , self.b + v2.b , self.c + v2.c) 

        return result  # here we are returning object Vector so it call __str__ automatically
    

    def __mul__(self,v3):
         result= self.a * v3.a + self.b * v3.b + self.c * v3.c

         return result  # here we return int coz no Vector object needed coz mul give int
    

    def __str__(self):
        
        return f"({self.a},{self.b},{self.c})"




#Working on 3d Dimensions @@Testing Implementations 
v1=Vector(2,3,4)
v2=Vector(4,5,6)
v3=Vector(3,4,7)


print(v1+v2)
print(v1*v3)