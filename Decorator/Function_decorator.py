
#Explanation in NotePad

# Use to modify the function without changing actual code 
# and it is use so we do not have to repat the code again and gain
# Decorator is a function that take anotheer function a argument and return the function

#! There is no use of class so easy for data hding and fast
# example


def callfunc_decorator(func):  # it goes to @ callfunc_decorator

    def callfunc2(*args):  # this Is wrappper
        print("Before")
        func(*args)
        print("After\n")
    
    return callfunc2  #this return runs when callfucn_decorator calls this goes jahan se call kiya hai mean add=callfunc2 also remember this return is inside callfucn_decorator






@callfunc_decorator
#the decorator change the function internally like this 
# add=@callfunc-decorator(add) --- This call callfucn_decorator(a=3,b=4)
#! after calling callfunc_decorator(a=3,b=4) the argument bind with the callfunc2()  but it not called yet
# Then it comes out and return callfunc2 then add= callfucn2 and run it

def add(a=3,b=4):   # when return add=callfucn2 then callfucn2 called and it prints
    print(a+b)

@callfunc_decorator
#sub=@callfunc-decorator(sub)
def sub(a=8,b=4):
    print(a-b)


add()
sub()
