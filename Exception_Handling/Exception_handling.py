




class testing():

    try:  #try–except here runs only ONCE — when the class is being CREATED,
          #NOT when methods are executed.

        def __init__(self,value):
            self.value=value

        

        def checking(self):

            print(self)

    

    except Exception as e:
        print(f"Your Error is {e}")  # here block not run coz try only check defination cratiton



obj=testing(3)

obj.checking()