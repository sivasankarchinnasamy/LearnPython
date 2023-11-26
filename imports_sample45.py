'''
__name__ is __main__ if this file is executed directly here. So "My mood is sad" gets printed
__name__ is imports_sample45 (when executed from 45.imports.py file using import statement)
if __name__=="__main__": is used to restrict localised execution
'''


def print_Sample(str):
    print(f"Reading from sample file. My mood is {str}")
print(__name__)
if __name__=="__main__":
    print_Sample("sad")