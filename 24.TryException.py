'''
Try except Exception basic example
'''
print("Type in any 2 numbers: ")
a=int(input())
b=int(input())

def exceptionTest():
    try:
        print("Value if a/b is: ",a/b)
    except Exception as e:
        print(e)

exceptionTest()