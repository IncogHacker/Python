

# else 
  # Means When try Block Run succesffuly Then Else work with try 

try:

    a=int(input("Enter The number"))

    print(a)


except Exception as e:

    print(f"Your code have Error {e}")



else:

    print("Your Code Executer Well")