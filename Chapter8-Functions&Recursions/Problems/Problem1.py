# Write a program using functions to find greatest of three numbers.
lista=[]

def greater_call(number):
    for x in range(number):
        enter=int(input(f"Enter The {x} NUmber--"))
        lista.append(enter)


    print(max(lista))













user_inputs=int(input("Enter the Number"))
greater_call(user_inputs)