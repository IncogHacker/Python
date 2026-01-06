class Employee:
 
         Employee_Salary="500000"  # This is A Class Attribute or Class Variable
         Employe_Position="SDE"
         Employee_Language="Python"


#! Attribute = kisi object ya class ki property (gun ya detail)

Employe_Name=Employee() # Creating an object (instance) of the Employee class


Employe_Name.name="Rishabh" #This Employe_Name.name is A Instance Variable or attribute created from Class

#Creating ANother Instance 
Employe_Name.Employee_Salary="0rs"


print(Employe_Name.name,Employee.Employe_Position,Employe_Name.Employee_Salary,Employee.Employee_Salary)
