


def calling():

    a=3
    b=3

    return a+b


if __name__=="__main__":
    print("This code is run directly run not from importing or exporting the module")
    print(calling())

    
    print(f"Your file from where you code is run {__name__}")