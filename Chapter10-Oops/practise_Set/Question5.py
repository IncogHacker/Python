# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 



import random

class IndianRailway:

    def __init__(self,Train_name,Ticket_Fare,Available_Seats):

        self.Train_name=Train_name
        self.Ticket_Fare=Ticket_Fare
        self.Available_Seats=Available_Seats

    def toget_Train_name(self):
        print(f"Train Name : {self.Train_name}")
    

    def toget_Fare(self):
        print(f"Ticket Fare: {self.Ticket_Fare}")
    
    def toget_Seats(self):
        if self.Available_Seats>0:
            print(f"Ticket Booked✅")
            print(f"{self.Available_Seats}--Seats Are available")



seatsrandom=random.randint(50,200)
object=IndianRailway("Rajdhani-Express",1500,seatsrandom)

object.toget_Train_name()
object.toget_Fare()
object.toget_Seats()


