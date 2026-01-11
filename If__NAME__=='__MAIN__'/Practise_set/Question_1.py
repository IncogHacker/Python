#  Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not 
# present, a message without exiting the program must be printed prompting the same



class File_existance:


    def file_1(self):
        try:
            #?   r tells Python: “Do NOT treat backslashes (\) as escape characters.”
            # An escape character is a special character (written using \) that tells Python to perform a special action inside a string.

              path=r"C:\Users\risha\Desktop\Python\If__NAME__=='__MAIN__'\Practise_set\Files_create--Question1\1.txt"
              with open(path,"w+") as file1:
                   
                   file1.write("Hi This iS first File")
                   file1.seek(0)
                   print(file1.read())

        
        except Exception as e:
             print(f"Error is--{e}")

    def file_2(self):
         try:
              
              path=r"C:\Users\risha\Desktop\Python\If__NAME__=='__MAIN__'\Practise_set\Files_create--Question1\2.txt"

              with open(path,"w+")as file_2:
                   file_2.write("this is Second file")

                   file_2.seek(0)
                   print(file_2.read())

         except Exception as e:
              print(e)


    def file_3(self):
        
         try:
              
              path=r"C:\Users\risha\Desktop\Python\If__NAME__=='__MAIN__'\Practise_set\Files_create--Question1\3.txt"
              with open(path,"r")as file_3:
                  print(file_3.read())
         except Exception as e:
              print(e)

         print("thank You program is NOt crashed")

obj=File_existance()

obj.file_1()
obj.file_2()
obj.file_3()










