

class cars:
    Engine="50cc"
    tyre="Rubber"
    colour="Black"

    def getinfo(self):
        print(self.Engine,self.car1)

        #self is must if we not write self then it will give error


obj=cars()
obj.car1="Lambhirghni" # instance attribute or object particular object property
obj.car2="Urus_Lambhorghini"

obj.getinfo()  #!! OR we can say cars.getinfo(obj) where obj==self