"""
Fibonacci
0 1 1 2 3 5 8 13 21 34.......
0 1 2 3 4 5 6 7  8 
"""

fibo = int(input("Enter the fibonacchi number: "))

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(fibo))


"""
Recursively Searching a Tree
-----------------------------

search(value_to_find, current_node):
    If current_node.value == value_to_find:
        print(‘value found:’, current_node.value)
    Else If current.node.has_children:
        search(value, current_node.left)
        search(current_node.right)
"""