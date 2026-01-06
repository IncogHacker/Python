sending=input("Enter The String")
y=len(sending)

for x in sending:
    if (x==" "):
        y-=1
    
if(y >=10):
 print("Your String is Gretaer then 10")
else:
 print("Your string Is not greater Then 10")