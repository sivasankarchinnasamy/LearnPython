list1=[1,2,3,4,5,6,7,8,9]

def filter_lessthan_4(i):
    return i<4

filtered_list = list(filter(filter_lessthan_4,list1))
print(filtered_list)