
name="0123456789"


print(name[1:7])


# ! [start : stop : step]
# !start = 1 → means start from index 1 ('1')

# !stop = 7 → means stop before index 7 (so last index used is 6)

# !step = 3 → means jump 3 characters forward each time


print (name[1:7:3])  

#[1:7] --- give 123456
#[1:7:3] --- give "14"  like start with 1 then skip 3 values  the get 4
#? → Move 3 steps ahead (1 + 3 = 4) → index 4 → '4'
#? → Again +3 (4 + 3 = 7) → stop before 7 (so stop here)



name_2="0123456789"

print(name_2[4:7:2]) # gives 46     
                   


