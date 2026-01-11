

# It assigns a value to a variable AND returns that value at the same time.
#this operator is use to use assign variable where we are doing any logical statements like if


#! Normal assingments 

# ? n=[1,2,4,5]
# ? x=3

# ? if len(n) >x:
#       ? print(f"{len(n)}--is greate Then 3")



# --------------------------------------

#! Walrus operator
if (n:=len([1,2,3,4]))>3:

    print(f"{n}--is greate Then 3")