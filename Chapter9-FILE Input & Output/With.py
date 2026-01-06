
# Best Method To open and read file using with statement it automatically open and close file 


with open("./Chapter9-FILE Input & Output/read.txt","r") as file:

    text=file.read()
    print(text)

