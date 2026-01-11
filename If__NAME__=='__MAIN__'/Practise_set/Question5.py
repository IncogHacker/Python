

# Store the multiplication tables generated in problem 3 in a file named Tables.txt. 


from Question3 import func

with open("Tabel.txt","w+") as file:

    list=func()
    print(list)

    file.write(str(list))  # now it store in text
    file.seek(0)
    file.read()





 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
# 