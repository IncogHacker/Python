


class parent1:

    def __init__(self):
        
        print("Hi")

        super().__init__()

class parent2:

    def __init__(self):
        
        print("This Side Rishabh")



class child(parent1,parent2):
    pass


object=child()  # only calls hi from parent one coz of method resolution order

