l = 10 # Global variable
def simpleTest():
    l=5 # Local variable
    m=8
    print( str(l)+" & "+str(m))
print( str(l))

simpleTest()
print( str(l))

print("**********************************************************************************")

s = 20 # Global variable
s=s+5
def newSimpleTest():
    global s # Global keyword allows global variables to be changed
    s=s+5 # Global value changed
    n=7   # Local variable
    print(str(s)+" & "+str(n))

print(str(s)) # Before change
newSimpleTest()
print( str(s)) # After change

print("**********************************************************************************")