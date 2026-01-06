import os

print(os.getcwd())


my_file = open(r"./Chapter9-FILE Input & Output/read.txt","r")
 # r= r is a raw string in python Normally, Python treats \n, \t, \u etc. as special characters.But when you add r before the string:
data = my_file.read()
print(data)

my_file.close()  # when ever we open file we should close it..if we dont close it still my file runs


