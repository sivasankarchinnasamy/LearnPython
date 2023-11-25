'''
args are used for passing many arguments to a fucntion
format fuction(normal_argument, *arg, **kwargs) # cant change order of arguments. First normal arguments, then *args, end **kwargs
*args - Should be list
**kwargs should be dictionary
'''

def argsDemo(*arguments):
    print(type(arguments))
    for items in arguments:
        print(items)

args = ["One","Two","Three","Four","Five"]
# argsDemo(*args)

def argsDemo(arg1, *arguments):
    print(type(arguments))
    for items in arguments:
        print(items)
    print(arg1)

args = ["One","Two","Three","Four","Five"]
aargument1 = "Siva"
# argsDemo(aargument1,*args)

def kwargsDemo(arg1, *newArgs, **kwargs):
    print(type(arg1))
    print(type(newArgs))
    print(type(kwargs))
    for items in newArgs:
        print(items)
    for key in kwargs:
        print(key +" : "+ kwargs[key])
    print(arg1)
arg1 = "Sivasankar"
newArgs = ["1","2","3","4","5"]
kwargs = {"1":"one","2":"two","3":"three"}

kwargsDemo(arg1,*newArgs, **kwargs)
