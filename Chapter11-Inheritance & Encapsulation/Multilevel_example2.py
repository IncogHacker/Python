
class employee:
    a=0


class programmer(employee):
    b=1

class manager(programmer):
    c=2


x=employee()
print(x.a)

y=programmer()
print(y.a,y.b)

z=manager()  #this is  Multilevel inheritance 
print(z.a,z.b,z.c)

