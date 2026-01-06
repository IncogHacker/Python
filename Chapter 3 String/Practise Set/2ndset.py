
Empolye_name=input("Enter Your Name")

print(f"Dear{Empolye_name}\n You are Selected! \n 12/01/2025")


# We cam also do like this 

letter = '''
       Dear <|Name|>, 
       You are selected! 
       <|Date|> '''

print(letter.replace("<|Name|>","Rishah Singh").replace("<|Date|>","12/02/2025"))

