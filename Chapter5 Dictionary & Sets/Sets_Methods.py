
s={1,2,3,4,5,6,7,8}

s.add(566)

print(s,type(s))

#length methods
print(len(s))


#remove method
s.remove(566)
print(s)


#pop()
s.pop()
print(f"This is after the Pop{s}")  # remove the first set value

#remove()
s.remove(8)
print(f"This is After remove {s}") # remove the selected value