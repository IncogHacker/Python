





p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

user_input=input("Enter The User Input")

if((p1 in user_input) or (p2 in user_input) or (p3 in user_input) or (p4 in user_input)):
    print("Your Message Is Spam")

else:
    print("Your Message Is  NOt Spam")

