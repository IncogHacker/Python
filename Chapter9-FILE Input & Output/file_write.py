

write_file="This is The File That We are Creating"


create=open("./Chapter9-FILE Input & Output/write.txt","w")

# ./ means:::::::::: "Start from the current folder where Python is running.

create.write(write_file)

create.close()