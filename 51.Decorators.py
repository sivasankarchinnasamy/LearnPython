def decorator_func(func):
    print("Before execution")
    func()
    print("After execution")

#decorator_func(who_is_siva) # This statement is same as @decorator_func

@decorator_func
def who_is_siva():
    print("Siva is a good boy")