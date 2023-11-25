# F Strings

# Normal string operatiom
import math


name = 'siva'
a="Name is : %s"%name
print(a)

# Another string operation using tuple - Issue is it is not readable for big tuple
name1 = "Siva"
name2 = "Ramya"
b= "%s & %s are a couple"%(name1,name2)
print(b)

# Using fortmat()
var1 = "Ramya"
var2 = "Siva"
c= "{0} & {1} are a couple" # We can change position by changing numbers  like {1} & {0}
d=c.format(var1,var2)
print(c.format(var1,var2))
# print(d)

# Using F Strings
# F stands for Fast
# Why F Strings better ? - You can do operations within string and also its faster
var3 = "Ram"
var4 = "Sundar"
e=f"{var3} & {var4} are brothers. Sin(90) is {math.sin(90)}"
print(f"{var3} & {var4} are brothers. Sin(90) is {math.sin(90)}")
# print(e)


