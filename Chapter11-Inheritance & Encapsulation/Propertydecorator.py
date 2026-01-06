

# It is mainly used for encapsulation. to acces the data through hidden function or data hinding

# 👉 @property lets you access a method like a variable its like a mummy who gives toy without her direct acces to toy
# 👉 It is used for controlled access to class data



#!here We see we access the toy car directly 
# class mummy:

    
#     def Toyss(self):
#         print(f"Your toys are Here:{self.toy}")




# obj=mummy() 

# obj.toy="car"  # toy=mummy(obj)

# obj.Toyss()


#!
class mummy:

    @property #The next function should behave like a VARIABLE, not like a function ”
    def Toyss(self):
        print(f"Your toys are Here:{self.toy}")

        return self.toy




obj=mummy() 

obj.toy="car"  # toy=mummy(obj)

# obj.Toyss()  #!property is not called by like a function

print(obj.Toyss) #! here we are calling as function which seem like variable and do not directly acces the toy it go to the property then return the actual data

#  Normal function → you CALL it
# 🔹 Property → Python CALLS it for you


