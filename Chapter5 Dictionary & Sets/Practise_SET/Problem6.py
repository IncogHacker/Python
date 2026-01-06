#Can you change the values inside a list which is contained in set S?  
#   No we can not coz list are mutable it can not be inside the set


 
s = {8, 7, 12, "Harry", (1,2)} 

s.remove((1,2))
s.add((3,2))

print(s)


  
