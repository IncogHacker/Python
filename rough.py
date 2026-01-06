




class Solution(object):
    def lengthOfLongestSubstring(self):
        # """
        # :type s: str
        # :rtype: int
        # """
        print(f"here Your Input---{self.inputs}")
        store=self.inputs

        
        add=1
        actual=0
        for x in range(len(store)-1):
            if store[x] != store[x+add]:
                actual+=1

        
        print(f"Actual length---{len(store)}")
        print(f"After Removing duplicates length--{actual}")

        
       

       
            
        

    
count=Solution()
count.inputs=input("Enter The Words You Want to Counts")
count.lengthOfLongestSubstring()
    
    

    



















       
        
