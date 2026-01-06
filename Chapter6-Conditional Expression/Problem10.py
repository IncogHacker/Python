# Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        => F


def System(Store):
 
 for marks in Store:
  
   if(marks>=90 and marks<=100):
       Grade="EX"
   elif(marks>=80 and marks<=90):
       Grade="A"
   elif(marks>=70 and marks<=80):
      Grade="B"
   elif(marks>=60 and marks<=70):
      Grade="C"
   elif(marks>=50 and marks<=60):
      Grade="D"
   else:
      Grade="FAIL"

   print(f"Marks: {marks} → Grade: {Grade}")




Bio=int(input(f"Enter Your Biology Marks--   "))
Maths=int(input(f"Enter Your Maths Marks-- "))
Eng= int(input(f"Enter Your English Marks-- "))
CS=int(input(f"Enter Your Computer Science Marks-- "))

Store=[Bio,Maths,Eng,CS]
System(Store)
