

class employee:

    a=1
    @classmethod
    def show(self):
        print(f"This shows--{self.a}")
    

obj=employee()
obj.a=45

obj.show() # if we do this then we get instance attribute a=45 but when use @classmethod the class attribute prints like a=1 show it only acceee the class attribute thats why we use class attribute