
#Explanation in NotePad

# Use to modify the function without changing actual code 
# and it is use so we do not have to repat the code again and gain
# Decorator is a function that take anotheer function a argument and return the function


# example


def callfunc_decorator(func):  # it goes to @ callfunc_decorator

    def callfunc2(*args):  # this Is wrappper
        print("Before")
        func(*args)
        print("After\n")
    
    return callfunc2  # this goes jahan se call kiya hai






@callfunc_decorator
#the decorator change the function internally like this 
# add=@callfunc-decorator(add)
#! then it call the add function and runs callfunc2 and also gives arguments to callfunc2 coz callfunc_decorator return callfunc2
def add(a=3,b=4):
    print(a+b)

@callfunc_decorator
#sub=@callfunc-decorator(sub)
def sub(a=8,b=4):
    print(a-b)


add()
sub()
