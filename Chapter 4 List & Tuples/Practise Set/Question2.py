marks=[]
for x in range (1 ,7):
    Entry=int(input(f"Enter The marks Of Student {x+1}:: "))
    marks.append(Entry)
    marks.sort()
print(marks)

