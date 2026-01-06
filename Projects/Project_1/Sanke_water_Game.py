import random
import time

def Sna_ke(x):

    computer=random.choice([1,-1,0])
    if(computer == 1):
        print(f"Your computer Choose ----Snake ")
    if(computer == -1):
        print(f"Your computer Choose ----Water ")
    if(computer == 0):
        print(f"Your computer Choose ----Gun")
        
    

    Values_games={

        "snake" : 1,
        "water" : -1,
        "gun"    : 0
          }
    me=Values_games[x]

   
    if computer==1 and me==-1:
        time.sleep(1)
        print("You Win computer Loose")

    elif computer ==-1 and me ==1:
        time.sleep(1)
        print("computer won you loose")

    elif computer == 1 and me == 0:
        time.sleep(1)
        print("computer win you loose")
    
    elif computer == -1 and me== 0:
        time.sleep(1)
        print("Computer win You loose")

    elif computer == 0 and me==1:
        time.sleep(1)
        print("You win computer loose")
    
    elif computer == 0 and me==-1:
        time.sleep(1)
        print("You win Computer loose")

    else:
        time.sleep(1)
        print("Draw")



x=input("Select the NUmber to defat Computer---")
Sna_ke(x)



