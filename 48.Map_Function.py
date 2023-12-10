'''
Map function is used to apply a common change to whole list
'''

# Example 1: Changing list of string to list of int w/o using Map function
list1 = ['1','2','3','4','5']
# print(list1) 
for item in range(len(list1)):
    list1[item]=int(list1[item])
# print(list1)

# Example 1: Changing list of string to list of int using Map function
list2 = ['1','2','3','4','5']
# print(list2)
list2=list(map(int,list2))  # map function returns object. So it always needs to be type cast as list. So its always list(map()) format
# print(list2)

# Example 2: Applying list of function using Map function - Get Square & Cube of numbers in a list

def square(a):
    return a*a
def cube(a):
    return a*a*a

func_list =[square,cube]
for i in range(5):
    sq_cube_list = list(map(lambda x:x(i), func_list ))
    print(sq_cube_list)