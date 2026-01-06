# Can we have a set with 18 (int) and '18' (str) as a value in it?

empty_set=set()

empty_set.add(18)
empty_set.add("18")

print(empty_set)  #{18, '18'} Ye we cn add int and string in a set together