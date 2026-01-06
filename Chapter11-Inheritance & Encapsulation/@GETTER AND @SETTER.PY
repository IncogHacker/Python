
#Getter ===Property


class callG_S:

    @property
    def private(self):     # this iS getter we are getting the value

        return f"{self.Fname}{self.Lname}"  #The getter’s return value is NOT used unless you ACCESS the property.means here its not in use
    
    @private.setter
    def private(self,value):        #Setter 
        
        self.Fname=value.split(" ")[0]
        self.Lname=value.split(" ")[1]


obj=callG_S()

obj.private="Rishabh Singh"  # here Setter calls to set the value not a normal assignment 
#it acts behind like this 
#!callG_S.private(obj,"Rishabh Singh")

print(obj.Fname,obj.Lname)



