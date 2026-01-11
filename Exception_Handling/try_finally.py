

# try–finally is used to guarantee that some code will always run,
# whether an error occurs or not.
# Finally mainly use in function like if we return the code finally still runs

def test_finally():
      
    try:

        a=int(input("Enter The NUmber"))
        return a


    except Exception as e:
       print(e)
       
       return

    finally:

     print("af")




test_finally()

    