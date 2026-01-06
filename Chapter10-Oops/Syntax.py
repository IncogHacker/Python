
# Creating A class 

class Employe:
     
     language="Python" #-These Two are Class Variables
     Salary="200000"


#  Creating a object (In one class Infinite number of objects can present)

#!Creating first object
Name1=Employe()
Name1.name="Rishabh"
                                            # name is NOT in the class

                                            # Python creates it only for this object

                                            # This is called an instance (object) variable

# Name1.name → found in object

# Name1.language → not in object → found in class

# Name1.Salary → not in object → found in class

print(Name1.name,Name1.language,Name1.Salary)


#!Creating second object
Name2=Employe()
Name2.name="Parth"
print(Name2.name,Name2.language,Name2.Salary)


