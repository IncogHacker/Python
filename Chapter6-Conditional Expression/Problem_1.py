

# if elif else ladder 

user_age=int(input("Enter The age"))

if(user_age>=23 and user_age<=60):
    print("You are Young")

elif(user_age<0):
    print("Age is less then 0 is Not possible")

elif(user_age>60):
    print("You are Old")
    
else:
    print("Youa are baccha")