
# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

empty_dictionary={}

for x in range(3):
    user_input_Key=str(input("Enter The Name--"))
    user_input_Value=str(input("Enter The favourite Language--"))

    # empty_dictionary.update({user_input_Key : user_input_Value})

    empty_dictionary[user_input_Key]=user_input_Value

print(empty_dictionary)