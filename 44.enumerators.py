'''
Enumerator is used to get both index and values from a data structure
No need to use : position=position+1 to iterate
'''

grocery = ["Rice","wheat","Sugar","Milk","Water"]

# Get odd itmes With out use of enumerator
print("Get odd itmes With out use of enumerator")
position = 0
for items in grocery:
    if position%2 == 0:
        print(grocery[position])
    position=position+1


# Get odd itmes with enumerator
print("Get odd itmes with enumerator")
for index, values in enumerate(grocery):
    if index%2==0:
        print(grocery[index])
    