# Write a program to find the greatest of four numbers entered by the user.
lista=[]
for x in range(4):
    user_input=int(input("Enter The Numbers\n"))
    lista.append(user_input)
print(f"You Entered Number Are ----- {lista}\n")

# greatest=lista[0] # here Give 0 coz index start with 0
# for num in lista:
#     if(num>greatest):
#         greatest=num
# print(f"Greatest Number is {greatest}")


# We can also Do like this ..

print(f"Gretest Number is {max(lista)}") # easisest way

