# Type hints in Python tell what type of value a variable, parameter, or return value should have.
# They do NOT change runtime behavior—they help readability, debugging, IDEs, and interviews


#? n : int=3  # Assigning as integer called Type hint here

#? print(n)

# ____________________________________________-

#! x : str="3"

#! print(type(x))





# -------------

def sum(a : int , b : int) -> int: # this means it returing the integr

    return a+b



print(sum(4,3))
