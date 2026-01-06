# Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up!

dictionary={
    "tamatar" : "Tomato",
    "pagal"  : "Crazy",
    "gadha"  : "Donkey"
    
}

user_look=input("Which word You want to english word--->")

meaning=dictionary.get(user_look)  # this only search for key not value and get return none when no found

# print(f"Your English Word is {meaning}")


# -------This is when we write value o it find the key of dictionary-----------------------------------------------

if meaning is None:
   for hindi ,english in dictionary.items():
      if english==user_look:
         meaning=hindi
         break

print(f"Your English Word is--{meaning}")



