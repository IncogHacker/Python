#  Create a class with a class attribute a; create an object from it and set ‘a’ 
#  directly using ‘object.a = 0’. Does this change the class attribute?


#! the answer is no the class attribute is not changed 


class demo:
   a=4




object=demo()

object.a=0

print(demo.a)
print(object.a)
















# this is made by me another

# class new:

#     def __init__(self):
     
#      self.a=""

#      print(f"{self.a}")

#     def show(self):
#        print(f"{self.a}")
        


# object=new()
# object.a=0

# object.show() # show() prints the current value of self.a



