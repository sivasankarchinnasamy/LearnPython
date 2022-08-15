print("Hello World")
'''Type Casting Examples
int()
float()
str()
'''
var1 = '30'
var2 = '50'
print(var1+var2)
print(int(var1)+int(var2))

'''
input() - arguments always come as string
'''
print("Enter any number: ")
ipnum = input()
print("Entered number + 10 is: "+ str(int(ipnum)+10)) # concat only works for string
print("Entered number + 10 is: ", int(ipnum)+10) # int passed as argument