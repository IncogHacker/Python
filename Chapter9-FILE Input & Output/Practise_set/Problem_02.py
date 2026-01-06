# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

import random ,time

def high_score(value):

    random_value=random.randint(984,1000)
    print(f"Your Score ---{random_value}")

   
    ## Reading a File To See Content Present Or Not
    try:
         data=open("./Chapter9-FILE Input & Output/Practise_set/HighScore_Data.txt","r")
         content=data.read()
         print(f"Your Previous Score ---{content}")
         data.close()

         if content =="":
              reading_highScore=0
         else:
              reading_highScore=int(content)
                
    
    except FileNotFoundError:
         reading_highScore=0


    if value == 1:
         if(random_value>reading_highScore):
          data=open("./Chapter9-FILE Input & Output/Practise_set/HighScore_Data.txt","w")
          score=data.write(str(random_value))
          print(f"Wow its a Highest Score is {random_value}")
          data.close()
         
    
    else:
         print("Game Is End")
        
         

         

user_value=int(input("Enter The 0  or 1 To Start the Game---"))
high_score(user_value)