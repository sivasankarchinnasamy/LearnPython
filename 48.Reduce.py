from functools import reduce
from sys import intern

list1 = [1,2,3,4,5,6]

# to get sum all the items in list1
sum_list1 = reduce(lambda x,y: x+y,list1)
print(sum_list1)

# to get product all the items in list1
product_list1 = reduce(lambda x,y: x*+y,list1)
print(product_list1)