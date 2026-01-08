


# Shape X

rows=6
column=6

def callX_shape():
 for i in range(rows):
    for j in range(column):
      if i==j or j==column-1-i:
        print("x",end="")

      else:
        print(" ",end="")
    print() # This Breaks The line 



callX_shape()      
      
      




        