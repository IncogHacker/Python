

# ! Write a program to store seven fruits in a list entered by the user.


# user_input=input("Enter The Fruits")

# lists_store=[user_input]

# # print(user_input)

# print(lists_store)


# ? Second Method

# fruits=[]

# f1=input("Enter The Fruit One")
# fruits.append(f1)

# f2=input("Enter the Fruit two")
# fruits.append(f2)

# f3=input("Enter the Fruit Three")
# fruits.append(f3)

# f4=input("Enter The Fruit four")
# fruits.append(f4)

# f5=input("Enter the fruit five")
# fruits.append(f5)

# f6=input("Enter The fruits Six")
# fruits.append(f6)

# f7=input("Enter the fruits Seven")
# fruits.append(f7)


# print(fruits)



# Third Method

fruits_store=[]
for i in range(5):  #range(start, stop, step)
    fruits = input(f"Enter Yout Fruits Names {i+1}: ")
    fruits_store.append(fruits)

    print(fruits_store)  # if it identation is here it print list on by one

print(fruits_store) #if it identation is here it print list after 7 time loop run only change in indetation