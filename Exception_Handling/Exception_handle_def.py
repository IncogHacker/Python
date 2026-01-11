




class testing():

   

        def __init__(self,value):
            self.value=value

        

        def checking(self):
              
              try:
                    print(self.x)

              except Exception as e:
                    print(f"Your err is {e}")  # this gives errro
            

              print("Thank you")





obj=testing(3)

obj.checking()