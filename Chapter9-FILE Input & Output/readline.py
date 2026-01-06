

# here if we use readline function then it gives in form of list 

# file_read=open(r"./Chapter9-FILE Input & Output/read.txt")

# store=file_read.readlines()  # so readline gives list and read give String

# print(store,type(store))




#! readline and readlines are different 
# ________________________________________________________________________
# Printing Line One by one 

open_file=open("./Chapter9-FILE Input & Output/read.txt")

# line1= open_file.readline()
# print(line1,type(line1))

# line2= open_file.readline()
# print(line2,type(line2))

# line3= open_file.readline()
# print(line3,type(line3))


# we can also do usig while loop 


line= open_file.readline()

while(line !=""):
     print(line)
     line=open_file.readline()

 
open_file.close()
