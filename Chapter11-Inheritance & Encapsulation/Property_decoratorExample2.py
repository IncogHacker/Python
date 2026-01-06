



class private_access:

    @property
    def call(self):

        print(f"here Your choclates after private access")
        return self.ename
    





obj=private_access()

obj.ename="Rishabh Singh"

print(obj.call)  # here return self.ename comes 