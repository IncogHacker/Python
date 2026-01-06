
# Create a class “Programmer” for storing information of few programmers 
# working at Microsoft. 

class Programmer:

    company="Micrsoft"

    def __init__(self,name,salary,Role):

        self.name=name
        self.salary=salary
        self.Role=Role

        print(self.name,self.salary,self.Role)


obj=Programmer("Rishabh","1lakhs","Software development engineer")
obj1=Programmer("Prateek","2lakhs","FrontEnd Engineer")


