

import random


class Guessiing_game:
    
    def __init__(self,value):

        self.value=value

    
    def Random_generator(self):

        random_x=random.randint(1,1000)
        self.random=random_x
        print(f"Your Computer Generated Number is--{self.random}")

    def checker(self):
          
          no_of_guesses = 0

          while True:# Always TRUE → loop starts
            value = int(input("Enter your guess: "))
            no_of_guesses += 1

            if value > self.random:
                print("Value is High..")

            elif value < self.random:
                print("Value is Low..")

            else:
                print(f"🎉 Congratulations! You guessed it in {no_of_guesses} attempts")
                break

                
           
        

obj=Guessiing_game(int(input("Enter The Numbe for Matching---")))

obj.Random_generator()

obj.checker()



