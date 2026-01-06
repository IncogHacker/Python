# Write a python program using function to convert Celsius to Fahrenheit

def degree():
    select=int(input("Press 1 for Cels To farenhite -- Press 2 for farenhite To celsius"))

    if (select==1):
     cels=int(input("Enter The Celisus You Want"))
     
     convrF=cels*9/5+32
     print(f"After Conver Your farenhite Is {convrF}")




    if(select==2):
     far=int(input("Enter The frenhite You Want"))

     convrC=far-32*5/9
     print(f"Afte Conversion Your Celsius is{convrC}")


degree()