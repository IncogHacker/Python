# 3. Create a class ‘Employee’ and add salary and increment properties to it. 
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
# # which changes the value of increment based on the salary

class Employee:

    salary=40000


    @property
    def Salary_AfterIncrement(self):

         # GETTER → when we READ the property
        return self.salary 


    @Salary_AfterIncrement.setter
    def Salary_AfterIncrement(self,increment):

        self.increment = increment
        self.salary=increment+self.salary

        return self.salary
    

    def percentage_increase(self):
          

        percentage_inc=self.increment/(self.salary-self.increment)*100

        print(f"Percnetage Increase In Salary--{percentage_inc}")
    







obj=Employee()
print(f"Before Increment Salary--{obj.salary}")

# SET value (calls setter)
obj.Salary_AfterIncrement=5000

print(f"Total salary After Increment---{obj.Salary_AfterIncrement}")

obj.percentage_increase()


