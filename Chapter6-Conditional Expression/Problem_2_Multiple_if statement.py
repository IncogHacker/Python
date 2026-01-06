


# Even and Odd also Finding Age 

user_input=int(input("Enter Your Age ---\n"))

print(f"Your Entered Age Is ---{user_input}\n")

# Even and odd 

if(user_input%2==0):
    print(f"Your Entered {user_input} is Even ")
else:
    print("Your Age is Odd")
    # if statement first  ends here 

# ------------------------------------------------------------------

if(user_input>=18):
    print("You Are Adult")
elif(user_input<18 and user_input>0):
    print("You are Not an Adult")
else:
    print("age is not valid")

    #second if statments ends here