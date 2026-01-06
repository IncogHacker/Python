
# ! append method in list

lista=["Rishabh","Riya","Nandani","Bishnu"]

lista.append("Singh") # This append the Singh in last 

print(lista)  # here not  like string if we add then whole list is changed I mean to say original one also changed therefore list is Mutable



# !sort Method

lista.sort()  # this method sort by alphabet  like A B C D...
print(lista)


# !Reverse  method
integers=[1,2,3,4,5,6,7,8]
integers.reverse()
print(f"This reverse whole list {integers}")



# !insert methods
# this is integer after reverse [8, 7, 6, 5, 4, 3, 2, 1]

integers.insert(1,20)
print(f"After inserting the value is {integers}")



#! pop
# this is integer after reverse [8, 20, 7, 6, 5, 4, 3, 2, 1]

integers.pop(1)
print(f"after popiing at index one remove 20 a {integers}")

print(integers.pop(1))

# [8, 7, 6, 5, 4, 3, 2, 1]



#!remove

integers.remove(6)
print(f"This will directly remove the int without using index{integers} ")

# [8, 7, 5, 4, 3, 2, 1]
