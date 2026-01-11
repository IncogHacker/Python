#  Create a class (2-D vector) and use it to create another class representing a 3-D 
# vector


class Two_D_Vector:
    
    def __init__(objt,i,j):

        objt.i=i
        objt.j=j


    def show_Two_D_Vector(self):

     return f"Your Two D Vector value is--({self.i}i + {self.j})j"

        
        


class Three_D_Vector(Two_D_Vector):

    def __init__(self,obj1,k):

        super().__init__(obj1.i,obj1.j) #--> This initialize the Two_D_vector.__init__(obj2,obj1.i,obj2.i)

        self.k=k 


    def  Show_Three_D_Vector(self):
       
       return f"Your Three D Vector value is--({self.i}i + {self.j}j + {self.k}k)"
         
         
       

        




obj1=Two_D_Vector(i=int(input("Enter The i--")),j=int(input("Enter The J--")))

print(obj1.show_Two_D_Vector()) #here python converts in this Two_D_Vector.show_Two_D_Vector(obj1) --so obj1 have i an dj values

obj2=Three_D_Vector(obj1,int(input("Enter The K value--")))


print(obj2.Show_Three_D_Vector())

