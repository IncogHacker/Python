

# we can imports different types of list ,tuple,dict,union 

# these structure help other programmer to understand your code easily

from typing import List 
from typing import Dict
from typing import Union
from typing import Tuple



#advantages of this is 


values : list[int]=[1,2,3,4]

values2: dict[str,int]=( "age", 23)


values3: tuple[int,str,int]=(1,"Rishabh",23)

# Union is used in Python type hints to specify that a variable or function parameter can accept more than one data type.  Union does NOT store multiple values

values4: Union[int,str]= "ID123" 
values4=10

print(values4)  # --The old value "ID123" is discarded