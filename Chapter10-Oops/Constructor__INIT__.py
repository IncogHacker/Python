


class games:

    graphics="4gb RAM"
    Engine="Turbo Engine"

    def __init__(self,name,salarie,lastname): #also called dunder maethod which starts with double__(underscore)
        print("This Run Automatically Without Calling Function whenever we create a New Object called a __INIT__constructor")

        self.names=name
        self.salaries=salarie
        self.lastnames=lastname

        print(self.names,self.salarys,self.lastnames)


obj=games("Rishabh",50000,"Singh")
