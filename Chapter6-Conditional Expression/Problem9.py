

# Write a program which finds out whether a given name is present in a list or not

lista=[]

for x in range(4):
    user_input=input("Enter The Names \n")
    lista.append(user_input)

print(f"Your List is {lista}")

find_name=input("Enter The Name you want to find present In lista or NOt")

if find_name in lista:
    print("Your Name Is present")

else:
    print("Your Name Is not Present in lista")
