


n=int(input("Enter The number"))
store=1

      
for x in range(n-1) :

    store *= n
    n=n-1        # This Is for decrement We cannot write like this n--

print(store)
       
      