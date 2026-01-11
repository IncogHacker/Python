#  Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not 
# present, a message without exiting the program must be printed prompting the same


import os


class File_fucntion:



    def file_create(self):
        

        try:
            os.makedirs("Files_create--Question1",exist_ok=True)  # this is use to create a new file

            with open("./Files_create--Question1/1.txt","w")as file:

                 file.write("This is The First File")


            with open("./Files_create--Question1/1.txt","r") as x:

                print(x.read())
        
        except Exception as e:
            print(f"{e}")








obj=File_fucntion()

obj.file_create()