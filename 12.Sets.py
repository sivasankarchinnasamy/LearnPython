# Set vs List -> Set cannot have duplicates, but List can have.

s= set()
s= set([1,2,3,4,5,1])
print(s)

# Add & Remove values
s.add(6)
print(s)
s.remove(6)
print(s)