'''
Print patter: For n level
For True:
*
**
***
****
*****
For False:
*****
****
***
**
*
'''
print("Enter level of printing")
level = int(input())
print("Enter state of printing")
state = input()

if(state=='True'):
    counter = level-1
    for x in range(level):
        for y in range(level - counter):
            print("*",end="")
        print("")      
        counter = counter-1
else:
    for x in range(level):
        for y in range(level):
            print("*", end="")
        print("")
        level=level-1
        
