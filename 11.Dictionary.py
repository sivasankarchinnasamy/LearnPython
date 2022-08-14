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

# Delete using key
del dict["Phone"]
print(dict)