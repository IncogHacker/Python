

# Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 

inside_data="This is Fisrt Problem And Twinkle Twinkle Little Star"

probole01_file=open("./Chapter9-FILE Input & Output/Practise_set/problem01_file.txt","w+")

probole01_file.write(inside_data)

probole01_file.seek(0) # move cursor to first place so we can read again

reading=probole01_file.read()

print(reading)

# if "Twinkle" in reading:
#     print("Yes Present")
# else:
#     print("Not Present")3

count=0

for i in reading.split(): # Split use for  to make words eperate so esy for indexing['Hello', 'world', 'I', 'am', 'learning', 'Python']
    if i=="Twinkle":
        count+=1

print(f"Yes Present Twinkle-{count}-Times")



probole01_file.close()