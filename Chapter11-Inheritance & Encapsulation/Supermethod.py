



class Employee:

    def __init__(self):
        print("This is The parent Class")



class Manager(Employee):
    def __init__(self):
        print("this is Manager Class")
        super().__init__()  # it is used to run next function 


class Studnet(Manager,Employee):
    def __init__(self):
        print("This is Student Class")
        super().__init__()



obj=Studnet()
