

# Given 
#! array=[1,-2,3,6,7,9,20,56] This is a sorted array  
#!target is 56
#always find mid using index value

class Binary_search:

    def __init__(self,array,target):
        
        print(f"My array is {array}")

        

        start=0
        index_value=len(array)-1

    

        while start<=index_value:
            #! finding Mid values 
            mid_value= (start + index_value) //2 # double use so point not come 3.5 similar to 3

            if array[mid_value]==target:
                print(f"Your target is Prsent at index {mid_value}")
                return
                

            elif array[mid_value]<target:
                start=mid_value+1
                
            elif array[mid_value]>target:
                index_value=mid_value-1



object=Binary_search([1,-2,3,6,7,9,20,56],56)

