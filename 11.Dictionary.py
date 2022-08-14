# Dictionary is Key-Value pairs

dict ={}
print(type(dict))

# Add data to Dictionary
dict["Siva"]="Name is Sivasankar"
#print(dict)
dict["Phone"]= 9503181980
dict["Address"] = {"Street":"Anup Reddy Layout","Pincode":560048,"City":"Bangalore"}
#print(dict)

# Access each data using key
print(dict["Address"]["Street"])
print(dict["Siva"].split(" ")[2])

# Access using get() function
print(dict.get("Siva"))

# Delete using key
del dict["Phone"]
print(dict)

# Update data using update()
dict.update({"Phone":9503181980})
print(dict)
dict.update({"Phone":8904323564}) #updated phone number
print(dict)

# get Keys
list = dict.keys()
print(list) # gives tuple of keys

# get items
items = dict.items()
print(items) # gives tuple of items