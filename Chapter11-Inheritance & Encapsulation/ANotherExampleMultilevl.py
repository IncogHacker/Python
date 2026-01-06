


#multilevel inheritanc


class parent:

    def callfucn(self):
        print("hi there is parent")



class parent1(parent):
    def callfucn2(self):
        print("hi there is parent 1")



class child(parent1):
    def calfucn3(self):
        print("hi there is parent3")

    

obj=child()

obj.calfucn3()
obj.callfucn2()
obj.callfucn()

