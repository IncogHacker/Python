
#Encapsulation is an OOP concept that binds data and methods together and restricts direct access to data.
#encapsulation is used to hide data or we  can say we can not access the data directly we have to use method or function to acess the data


class Rupees:

    def __init__(self):
        
        self._cash=0
        self._withdraw=0

    @property
    def cash(self):
        return self._cash  # here cash is encapsulated
    
    @cash.setter
    def cash(self,value):
        self._cash=int(value)

        print(f" Your Account Balance Is {self._cash}")

    @property
    def withdraw(self):
         return self._withdraw  # here withdraw is encapsulated
    
    @withdraw.setter
    def withdraw(self,value):

        if int(value)>self._cash:
            print("\n Your Withdrawel Amount Is Higher")

            new_amount=int(input("Enter The New Withdrawel Amount--"))

            self.withdraw=new_amount

        else:
            self._withdraw=int(value)
            print(f"Sucessfully Withdraw--{self._withdraw}")
    







obj=Rupees()

obj.cash=int(input("Enter Your Cash--"))   # ! Setter runs first and only coz it sets the value(here it se setter assigment)property is only for show now for running propery we need to give obj.cash without assingment alag se wo bhi

obj.withdraw=int(input("Enter Your withdraw Amount--")) # this Call the setter coz whenever any assingment it call the setter






# _cash, _withdraw ------	Encapsulated data
# cash, withdraw-------	Public interface
# Validation in setter------	Security
# No direct access-------	Encapsulation
# Rules inside class-------	Data protection

