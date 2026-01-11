

#  Write a program to display a/b where a and b are integers. If b=0, display infinite by 
# handling the ‘ZeroDivisionError’



a=3
b=0

try:

    # if b==0:
    #     raise ZeroDivisionError("This is infinite Zerodivinsion error")
    # else:
        print(a/b)

except ZeroDivisionError as z:
    print(f"infinite--{z}")


