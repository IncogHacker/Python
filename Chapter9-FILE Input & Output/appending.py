

filesent="HI My name is rishabh singh"


fileA=open("./Chapter9-FILE Input & Output/append.txt","w+") # also use (a) for appending (+) for updating 

fileA.write(filesent)

fileA.write("and I am a Software development engineer") # here we are appending the file so

fileA.seek(0) #here seek move cursor to a specific position in a file....

store=fileA.read()

print(store)


fileA.close

