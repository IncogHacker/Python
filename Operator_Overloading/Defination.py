#Operator Overloading (simple & clear)

#!Operator overloading means giving extra meaning to an operator (+ - * == < etc.) for user-defined objects (classes).

# Normally operators work on int, float, string,
# but with operator overloading, they work on objects too.

# Why we need it

#!So that objects behave naturally, just like numbers.

# Example idea 👇
# If a + b works for numbers,
# then obj1 + obj2 should also work logically.

class operator_overloading:  # Basically adding Objects call operator overloading


    def __init__(self,value):  #__init__ is used to store values inside the object.
        self.value=value    
        # print(self.value)    #? both objects value stored like obj1(value) and obj2(value) both object stored there different values if we dont write init then no oe is here to recive the object argument and it will not run

    
    def __add__(self,value2):   # self-obj1 and value2 obje 2

        return self.value +value2.value

    



    



obj1=operator_overloading(int(input("Enter The Number")))

obj2=operator_overloading(int(input("Enter The NUmber")))

print(obj1+obj2)  #In memory obj1.__add__obj2 call the add function

# operator_overloading.__init__(obj1,5) # this is done internally by python it called by this way




#Dry Run Explain 

# ! Overview --->     class load → __init__ → __init__ → __add__ → print

# 1- Class Method initialize not run and Inside Class Method- All other Function Initialize but not run stored in memory

# 2- Now When obj1=operator_overloading(int(input("Enter The Number")))  is create Then Memory run __init__ 

      #!operator_overloading.__init__(obj1,10) Memory call like This
         # Now self.value=10 store Sowhere in memory Now then run object2 

#2- Now When obj2=operator_overloading(int(input("Enter The Number")))  is create Then Memory run __init__ 

      #!operator_overloading.__init__(obj2,20) Memory call like This
         # Now self.value=20 store here

         #? both 10 and 20 store in memory

#print(obj1+obj2)
        
        #! (+) detected between objects

        # ? So python converts obj1+obj2 into obj1.__add__obj2 then add function run  and add All the values


      

