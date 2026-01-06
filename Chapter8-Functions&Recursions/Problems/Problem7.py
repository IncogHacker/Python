# Write a python function to remove a given word from a list ad strip it at the same time.

import time
lista=[]
def listist(x):
    for i in range(x):
     name=input("enter the names")
     lista.append(name)
    print(lista)

    print(f"Your current List is {lista}\n")

    time.sleep(1)
    
    choice=input("You want to remove Word PRESS (W) or For Name Press (N)")
    if choice == "N" :
      removes=input(f"Which Name You want to remove from the list")
      lista.remove(f"{removes}")
      print(f"After Removing{lista} ")
    else:
      #Strip uses to remove Extra Spaces 

      letter=input(f"which letter You want to remove----").strip()
      for y in range(len(lista)):
          if letter in lista[y]:
             lista[y]=lista[y].replace(letter,"")
      print(lista)




user_input=int(input("Enter The Number"))
listist(user_input)