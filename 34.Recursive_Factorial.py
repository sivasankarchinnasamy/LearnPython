fac = int(input("Enter the number for Factorial: "))  # convert the input from String to int at the earliest

def factorial(fac):
    if fac==1:
        return fac
    elif fac>0:
        return fac*factorial(fac-1)

print(factorial(fac))
