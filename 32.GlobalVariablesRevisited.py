
def rohan():
    x = 10
    def harry():
        x =20
        print("value of inner x is :"+str(x))
    print("value of outer x is :"+str(x))
    harry() #calling nested function
    
rohan()

print("**********************************************************************************")
y=50  # if this line is removed, global y statement won't work. Program will throw error

def mohan():
    y = 10
    def barry():
       global y  # global keyword jumps to top of program file and looks for variable
       y=y+20
       print("value of inner x is :"+str(y))
    print("value of outer x is :"+str(y))
    barry() #calling nested function inside parent function
    
mohan()

print("**********************************************************************************")