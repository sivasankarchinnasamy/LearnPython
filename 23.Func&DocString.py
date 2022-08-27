'''
Docstring is the first line in a function, that can be accessed via funcName.__doc__
'''

def function1():
    ''' This is a doc string for function 1'''
    print("This is the body of Function 1")

def function2():
    print("This is the body of Function 2")
    return True 

print(function1.__doc__)

print(function1()) # Returns None as no return statement
print(function2()) # Returns True