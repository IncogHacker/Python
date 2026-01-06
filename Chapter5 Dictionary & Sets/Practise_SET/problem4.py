
s=set()

s.add(20)
s.add("20")
s.add(20.0)

print(s)  # {20, '20'}  #coz 20 == 20.0  coz python compare the value not the data type thats why bot are same and set ignore the 20.0

print(len(s))   # 2