# Dictionary is Key-Value pairs

import string


dict1 ={}
print(type(dict))

# Add data to Dictionary
dict1["Siva"]="Name is Sivasankar"
#print(dict)
dict1["Phone"]= 9503181980
dict1["Address"] = {"Street":"Anup Reddy Layout","Pincode":560048,"City":"Bangalore"}
#print(dict)

# Access each data using key
print(dict1["Address"]["Street"])
print(dict1["Siva"].split(" ")[2])

# Access using get() function
print(dict1.get("Siva"))

# Delete using key
del dict1["Phone"]
print(dict1)

# Update data using update()
dict1.update({"Phone":9503181980})
print(dict1)
dict1.update({"Phone":8904323564}) #updated phone number
print(dict1)

# get Keys
list = dict1.keys()
print(list) # gives tuple of keys only

# get items
items = dict1.items()
print(items) # gives tuple of keys & items - gets printed as tuple

for key in dict1:    # Default iterating dictionary gives keys as tuple
    print(key+" -> "+ str(dict1[key]))  # Convert all data types to string to print

for key in dict1.keys():  # Same as above
    print(key+" -> "+ str(dict1[key]))


list1 = [[1,'one'],[2,'two'],[3,'three'],[4,'four']]  # Extend list inside list

for key, value in list1:
    print("Key is: "+str(key)+ " value is: "+value)

print("-------------------------------------------------")

dict2= dict(list1)  # Printing Keys & Values
for key, value in dict2.items():
    print("Key is: "+str(key)+ " value is: "+value)