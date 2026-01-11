

from typing import Dict

# Merging two dictionaries


x: dict[str:int]={"Rishabh":23,"Riya":34}

y:dict[str:int]={"Nandani":23,"Vishnu":42}

merged=x|y  # Merging dictionaries

print(merged)