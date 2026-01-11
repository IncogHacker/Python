

# Write a program to print third, fifth and seventh element from a list using enumerate 
# function. 



list=[2,3,4,5,6,3,99,100]

for x ,item in enumerate(list):

    if x==2 or x==5 or x==6:

        print(x,item)