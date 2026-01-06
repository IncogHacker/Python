# Write a recursive function to calculate the sum of first n natural numbers.

def natural_numbers(n):

    
    if(n==1 or n==0):
         return 1
    else:
         return n + natural_numbers(n-1)

        






n=int(input("Enter the Natural NUmber You want the sum"))
print(f"Here are Your Natural Numbers{natural_numbers(n)}")
