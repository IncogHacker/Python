# Write a python function to print first n lines of the following pattern: 
# *** 
# **               - for n = 3 
# *

def stars(n):
    
    for x in range(n):
        if(n==1):
          return "*"
        print("*",end=" ")

    print("\n")
    return stars(n-1) # here we are doing recursion basically
        






n=int(input("Enter The NUmber"))
print(f"{stars(n)}")
