# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 

maxi_mum=100

sci=int(input("You English Marks --> \n"))
eng=int(input("You Science Marks --> \n"))
hin=int(input("You Hindi Marks --> \n"))

percent=sci/maxi_mum*100

if(percent<=33):
    print(f"Your Percentage is--{percent}% and you are  Failed in  Science")
else:
    print(f"You Are Passes in this Science and your percent is  {percent}%")


percent=eng/maxi_mum*100
if(percent<=33):
    print(f"Your Percentage is--{percent}% and you are  Failed in  English")
else:
    print(f"You Are Passes in this Science  and your percent is  {percent}%")

percent=hin/maxi_mum*100
if(percent<=33):
    print(f"Your Percentage is--{percent}% and you are  Failed in  Hindi")
else:
    print(f"You Are Passes in this Hindi and your percent is  {percent}%")





