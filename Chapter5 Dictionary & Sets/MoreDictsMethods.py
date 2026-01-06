

marks={
    "Rishabh" :34,
    "Riya Singh" :23,
    "Nandni Singh" :56,
    "Vishnu Singh":21,
}


print(marks.update({"Rishabh": 22})) # None

marks.update({"Rishabh": 23,"renuka":12}) # this change in the original dictionary coz it is mutable 

print(marks.items())


print(marks.get("Rishabh")) # this returns none if key is not present

print(marks["Rishabh"]) # this return error

