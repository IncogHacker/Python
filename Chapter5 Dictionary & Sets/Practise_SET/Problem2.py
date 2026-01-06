# Write a program to input eight numbers from the user and display all the unique 
#  numbers (once)

user_range = int(input("Enter The Range You Want the Number-->"))

empty_sets=set()

for x in range(user_range):
    user_input=int(input(f"Enter The {x+1} NUmber--- \n"))
    empty_sets.add(user_input)  # here apppend not work only add in sets

    print(f"You Selected Number Are {empty_sets}")  # give unique numbers coz set always give unique numbers

    

