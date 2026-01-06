


def recursion_factorial(n):
    if(n==0 or n==1):
        return 1
    return n * recursion_factorial(n-1)
    

n=int(input("Enter The Number You want the factorial"))
Store=recursion_factorial(n)
print(Store)