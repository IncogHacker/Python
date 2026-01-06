
#! lista=[]

#? for x in range(4):
#?     user_input=int(input(f"Enter The {x+1} Number::"))
#?     lista.append(user_input)

#? print(f"Your List Is {lista}")

#? for y in range(4):
#?     lista[y]= lista[y]+(y+1)   # this add 1 then add 2 then 3 and so on 

#?    # lista = [2, 3, 4, 5] --->lista = [3, 5, 7, 9]

#? print(f"After Sum Your List is {lista}")




# Write a program to sum a list with 4 numbers.

numbers=[]

user_range=int(input("Enter The Range---"))

for x in range(user_range):
    store=int(input(f"Enter The {x+1} Number"))
    numbers.append(store)

print(f"Your List is {numbers}")


print("\n Adding Your List")

for y in range(len(numbers)-1):
    numbers[y+1]=numbers[y]+numbers[y+1]

print(numbers[-1])




#! Another Method using built in functions

lista=[2,3,4,5]
print(sum(lista))













