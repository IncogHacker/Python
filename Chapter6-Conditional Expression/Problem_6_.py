# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# # to detect these spams



def check_spam():

    email=str(input("Enter The Mail You want To Send"))

    #!if(email.__contains__("Make a lot of money")):
    #     print("Your Mail Is SPam")

        # or We can also write like this 
    
    spam_message=["Make a lot of money","buy now","subscribe this","click this"]

    for words in spam_message:
         if words in email:   # it check like this "Make a lot of money" in "Click this to get rewards!"
          print("Your Message Is Spam")
          break
    
    else:
        print("Your Message Is Not Spam")
    
    
    
        



check_spam()