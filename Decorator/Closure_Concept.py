


# !A function that remembers variables from its outer function, even after the outer function has finished executing.

# Why closures are used

# !Data hiding (without class)  ---that is encapsulation 

# !Callbacks

# !Decorators

# !Functional programming


# 🔹 Closure vs Class (difference)
# Closure        	Class
# Lightweight	    Heavy
# No self	        Uses self
# Functional style	OOP style



def outer(x):
    def inner():
        print(f"This will print when inner Called only then it prints --{x}")

    return inner  #! This return inner goes to f=outer(10) == inner  so now f=inner 



f=outer(10) # here outer called and pass the variable 10 to outer(10) and here inner function automatically bind with outer variable(called a lexical binding) and store inner(10) but remeber inner not called yet


f() # here f=inner and it called inner now  and prints starts printing
