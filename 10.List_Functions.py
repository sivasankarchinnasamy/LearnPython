string_list = ["One","Two","Three","Four"]
number_list = [1,2,3,4,5,6]

# Functions sort() , reverse() modifies the list 
number_list.sort()
print(number_list)

number_list.reverse()
print(number_list)

# slicing does not modifies the list
print(number_list[1:4])
print(number_list)

# Extended Slicing
print(number_list[::-1]) # reverses list - use -ve extended slicing to reverse only
print(string_list[::-1]) # never use extended slicing >-1 ie don't use -2,-3 etc
print(number_list[0:3:-1]) # Does not work - return empty
print(string_list[0:4:-1]) # Does not work - return empty


# Mutable Vs Immutable 
# Tuple is immutable, but list is mutable
tp=(1,2,3,4)
# tp[1]= 5 #This won't work as it is immutable